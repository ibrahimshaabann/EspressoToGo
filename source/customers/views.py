# from django.db.models import Q
# from rest_framework import views, status
from rest_framework import viewsets, filters
from rest_framework.permissions import  AllowAny
# from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.response import Response
# from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
# from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
# from users.authentication import CustomUserAuthenticationBackend

from .models import Customer
from .serializers import CustomerSerializer

from .filters import CustomerFilter

class CustomerViewSetForAdmins(viewsets.ModelViewSet):
    """
    This viewset is used to perform CRUD operations on Customers By Admins.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAdmin, IsAuthenticated,)
    permission_classes = (AllowAny,)
    
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter, 
        filters.OrderingFilter,
    ]
    
    filterset_class = CustomerFilter


# class CustomerSignUpView(views.APIView):

#     """
#     This view is used to register a Customer. 
    
#     """

#     permission_classes = (AllowAny,)
#     throttle_classes = [UserRateThrottle, AnonRateThrottle]


#     def post(self, request):
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CustomerLoginView(views.APIView):
#     """
#     This view is used to login a Customer.
#     Using the email, phone_number, or username and the password.
#     Customers get thier access and refresh tokens at this endpoint.
#     """

#     permission_classes = [AllowAny,]
#     throttle_classes = [UserRateThrottle, AnonRateThrottle]


#     def post(self, request):

#         """
#         This method is used to login a Customer.
#         Simply by providing the email, phone_number, or username and the password.
#         We get them from only post requests.
#         We check by our custom authentication backend if the admin exists and the password is correct.
#         If so, we return the access and refresh tokens.
#         """

#         email_or_phone_or_username = request.data.get("email_or_phone_or_username")
#         password = request.data.get("password")

#         Customer = CustomUserAuthenticationBackend().authenticate(
#             request=request, username=email_or_phone_or_username, password=password
#         )

#         if Customer:
#                 access_token = AccessToken.for_user(Customer)
#                 refresh_token = RefreshToken.for_user(Customer)
#                 return Response(
#                     {
#                         "access": str(access_token),
#                         "refresh": str(refresh_token),
#                     }
#                 )
#         else:
#             return Response(
#                 {
#                     "error": "Invalid credentials",
#                 },
#                 status=status.HTTP_401_UNAUTHORIZED,
#             )
        