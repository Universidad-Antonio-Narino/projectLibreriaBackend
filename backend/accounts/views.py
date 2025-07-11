from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class RegisterView(APIView):
    def post(self,request):
        serializer = SignUpSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuario registrado exitosamente"},status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            tokens = serializer.validated_data
            
            data = {
                "msg": "Login exitoso",
                "user": {
                    "first_name": tokens.get('first_name', ''),
                    "last_name": tokens.get('last_name', ''),
                    "email": tokens['email'],
                    "Token_Access":tokens['access_token']
                }
            }
            response = Response(data,status=status.HTTP_202_ACCEPTED)
            response.set_cookie(key="refresh_token",
                value=tokens['refresh_token'],
                httponly=True,
                secure=False,  # Cambia a True en producción con HTTPS
                samesite='Lax'
            )
            response.set_cookie(
                key="access_token",
                value=tokens['access_token'],
                httponly=True,
                secure=False,  # Cambia a True en producción con HTTPS
                samesite='Lax'
            )
            return response
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request):
        response = Response(
            {'msg':'Logout Existoso'},
            status=status.HTTP_200_OK
        )
        response.delete_cookie("access_token")
        return response
    