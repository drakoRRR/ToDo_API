from MySQLdb import IntegrityError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import LoginSerializer, RegisterSerializer


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            username = serializer.data['username']
            first_name = serializer.data['first_name']
            last_name = serializer.data['last_name']
            password1 = serializer.data['password1']
            password2 = serializer.data['password2']

            if password1 != password2:
                return Response({
                    'status': 400,
                    'message': 'Passwords do not match',
                    'data': {}
                })

            try:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    password=password1
                )
            except IntegrityError:
                return Response({
                    'status': 400,
                    'message': 'Username already exists',
                    'data': {}
                })

            refresh = RefreshToken.for_user(user)

            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            })

        return Response({
            'status': 400,
            'message': 'Something went wrong',
            'data': serializer.errors
        })


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']

            user = authenticate(username=username, password=password)

            if user is None:
                return Response({
                    'status': 400,
                    'message': 'invalid password or username',
                    'data': {}
                })

            refresh = RefreshToken.for_user(user)

            return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                })

        return Response({
            'status': 400,
            'message': 'something went wrong',
            'data': serializer.errors
        })
