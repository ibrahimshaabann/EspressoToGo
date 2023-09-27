from django.db.models import Q

from rest_framework import views

from rest_framework import viewsets, filters

from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Employee
from .serializers import EmployeeSerializer

from .permissions import IsAdmin

from django_filters.rest_framework import DjangoFilterBackend

from .filters import EmployeeFilter


from rest_framework.response import Response
from users.authentication import CustomUserAuthenticationBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken



class EmployeeViewSetForAdmins(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAdmin, IsAuthenticated,)
    permission_classes = (AllowAny,)
    
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter, 
        filters.OrderingFilter,
    ]
    
    filterset_class = EmployeeFilter




class EmployeeSignUpView(views.APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeLoginView(views.APIView):
    
    """
    This view is used to login an Employee.
    Using the email, phone_number, or username and the password.
    Employees get thier access and refresh tokens at this endpoint.
    """

    permission_classes = [AllowAny,]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


    def post(self, request):

        """
        This method is used to login an employee.
        Simply by providing the email, phone_number, or username and the password.
        We get them from only post requests.
        We check by our custom authentication backend if the admin exists and the password is correct.
        If so, we return the access and refresh tokens.
        """

        email_or_phone_or_username = request.data.get("email_or_phone_or_username")
        password = request.data.get("password")

        employee = CustomUserAuthenticationBackend().authenticate(
            request=request, username=email_or_phone_or_username, password=password
        )

        if employee:
                access_token = AccessToken.for_user(employee)
                refresh_token = RefreshToken.for_user(employee)
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