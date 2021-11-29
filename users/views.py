# Imports
import jwt
import string

# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from django.db.models import Q
from django.contrib.auth import authenticate, password_validation


# Rest framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

# localApp
from django.conf import settings
from .serializers import ModelUserSerializer
from .custom_permissions import (
    UserAdminPermission,
    SuperAdminPermission,
    ManagerUserPermission,
    BecadoUserPermission
)
from .models import User


class UserViewSet(ModelViewSet):
    """
        Endpoints Base de usuario
    """
    serializer_class = ModelUserSerializer
    queryset = User.objects.filter(is_active=True)

    def get_permissions(self):
        """
            Permissions customs
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [
                IsAuthenticated,
                SuperAdminPermission |
                ManagerUserPermission |
                BecadoUserPermission
            ]

        if self.action in ['destroy', 'update', 'partial_update', 'create']:
            permission_classes = [
                IsAuthenticated,
                SuperAdminPermission |
                ManagerUserPermission
            ]

        if self.action == "login":
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def create(self, request):
        user_password = request.data.get("password", '')
        data_temp = {}

        if user_password == "":
            data_temp['password'] = User.objects.make_random_password(
                8, string.digits + string.ascii_letters)

        for key, value in request.data.items():
            data_temp[key] = value

        serializer = self.serializer_class(data=data_temp)
        if serializer.is_valid(raise_exception=True):
            try:
                user = serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                return Response(
                    {"message": e.args[0]},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {"message": serializer.error_messages},
                status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, pk=None):
        try:
            User.objects.get(id=pk).delete()
        except Exception:
            return Response(
                {
                    "message": "Error when deleting"
                }, status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {
                "message": "User deleted"
            }, status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['post'])
    def login(self, request):
        try:
            username = request.data.get('username', None)
            email = request.data.get('email', None)
            password = request.data.get('password', None)
            try:
                if email:
                    user = get_user_model().objects.get(email=email.lower())
                else:
                    user = get_user_model().objects.get(username=username)

                roles = user.roles.all()
                if not roles or user.is_active == False:
                    return Response(
                        {
                            "message": 'No access to the platform'
                        }, status=status.HTTP_200_OK
                    )

                valid = password == user.password or check_password(
                    password, user.password)
                if valid == False:
                    return Response(
                        {
                            "message": 'Invalid password or email'
                        }, status=status.HTTP_200_OK
                    )

                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
            except Exception as e:
                return Response(
                    {
                        "message": 'The user does not exist'
                    }, status=status.HTTP_200_OK
                )
        except Exception:
            return Response(
                {
                    "message": 'Error logging in'
                }, status=status.HTTP_200_OK
            )

        return Response(
            {
                "token": access_token,
                "username": user.username,
                "is_active": user.is_active
            }, status=status.HTTP_200_OK
        )
