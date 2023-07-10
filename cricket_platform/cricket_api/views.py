from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.db import models
from .serializers import AdminSignupSerializer
from .models import CustomUser

class AdminSignupView(APIView):
    def post(self, request):
        serializer = AdminSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = {
                'status': 'Admin Account successfully created',
                'status_code': status.HTTP_200_OK,
                'user_id': user.id
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminLoginView(APIView):
    def post(self, request):
        usernam = request.data.get('username')
        passwor = request.data.get('password')

        user = authenticate(request, username=usernam, password=passwor)
        print(user)

        if user is not None:
            login(request, user)
            response_data = {
                'status': 'Login successful',
                'status_code': status.HTTP_200_OK,
                'user_id': str(user.id),
                'access_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                'status': 'Incorrect username/password provided. Please retry',
                'status_code': status.HTTP_401_UNAUTHORIZED
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)