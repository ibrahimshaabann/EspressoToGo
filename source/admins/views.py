from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework import views, status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from users.authentication import CustomUserAuthenticationBackend

from .serializers import AdminSerializer
from .models import Admin

from rest_framework_simplejwt.authentication import JWTAuthentication


from .permissions import IsAdmin

class AdminSignUpView(views.APIView):
    # permission_classes = (AllowAny,)
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    permission_classes = (IsAdmin,)
    authentication_classes = (JWTAuthentication,)
    

    def post(self, request):
        request.data["role"] = "ADMIN"
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class AdminLoginView(views.APIView):
    
    """
    This view is used to login an admin.
    Using the email, phone_number, or username and the password.
    Admins get thier access and refresh tokens at this endpoint.
    """

    permission_classes = (AllowAny,)
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]


    def post(self, request):

        """
        This method is used to login an admin.
        Simply by providing the email, phone_number, or username and the password.
        We get them from only post requests.
        We check by our custom authentication backend if the admin exists and the password is correct.
        If so, we return the access and refresh tokens.
        """


    
        email_or_phone_or_username = request.data.get("email_or_phone_or_username")
        password = request.data.get("password")


        admin = CustomUserAuthenticationBackend().authenticate(
            request=request, username=email_or_phone_or_username, password=password
        )

        if admin and admin.role == "ADMIN":
                access_token = AccessToken.for_user(admin)
                refresh_token = RefreshToken.for_user(admin)
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
        



class AllAdminsViewSet(generics.ListAPIView):
    """
    This view is used to get all admins.
    """
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAdmin,)
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    # permission_classes = (AllowAny,)