from rest_framework.generics import  CreateAPIView
from rest_framework import permissions
from .models import User
from .serializer import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CreateListUser(CreateAPIView):
    """Class based generic view to create and list all users"""

    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# class SignInUser(TokenObtainPairView):
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = CustomTokenObtainPairSerializer