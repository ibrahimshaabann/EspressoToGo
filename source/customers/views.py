from rest_framework.permissions import AllowAny
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework import views, status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from users.authentication import CustomUserAuthenticationBackend

from .serializers import CustomerSerializer

from .models import Customer

from rest_framework import viewsets

from .filters import CustomerFilter

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters

from .permissions import IsAdmin

from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomerSignUpView(views.APIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAdmin,)
    permission_classes = (AllowAny,)

    def post(self, request):
        request.data["role"] = "CUSTOMER"   # This is to set the role to CUSTOMER when signing up.
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class CustomerLoginView(views.APIView):
    
    """
    This view is used to login a customer.
    Using the email, phone_number, or username and the password.
    Customers get thier access and refresh tokens at this endpoint.
    """

    permission_classes = (AllowAny,)
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]


    def post(self, request):

        """
        This method is used to login a customer.
        Simply by providing the email, phone_number, or username and the password.
        We get them from only post requests.
        We check by our custom authentication backend if the admin exists and the password is correct.
        If so, we return the access and refresh tokens.
        """


    
        email_or_phone_or_username = request.data.get("email_or_phone_or_username")
        password = request.data.get("password")


        customer = CustomUserAuthenticationBackend().authenticate(
            request=request, username=email_or_phone_or_username, password=password
        )

        if customer and customer.role == "CUSTOMER":
                access_token = AccessToken.for_user(customer)
                refresh_token = RefreshToken.for_user(customer)
                return Response(
                    {
                        "access": str(access_token),
                        "refresh": str(refresh_token),
                    }
                )
        else:
            return Response(
                {
                    "error": "Invalid credentials",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        



class AllCustomersViewSet(viewsets.ModelViewSet):
    """
    This view is used to get all admins.
    """
    permission_classes = (IsAdmin,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = (AllowAny,)    

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter, 
        filters.OrderingFilter,
    ]
    
    filterset_class = CustomerFilter