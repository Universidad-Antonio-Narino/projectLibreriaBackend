#from django.db.models import Q  for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import UserLibrary
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

#serializer.Serializer is better to register and login operations
class SignUpSerializer(serializers.Serializer):
    password = serializers.CharField(min_length = 8,max_length=16,style={'input_type':'password'},write_only=True)
    #valida que el campo ingresado no exista en dba UniqueValidator
    cedula = serializers.CharField(required = True,validators=[UniqueValidator(queryset=UserLibrary.objects.all(),message='Usuario existente')])
    email = serializers.EmailField(required = True,validators=[UniqueValidator(queryset=UserLibrary.objects.all(),message='Usuario existente')])
    username = serializers.CharField(required = True,validators=[UniqueValidator(queryset=UserLibrary.objects.all(),message='Ese nombre de usuario ya esta en uso')])
    first_name = serializers.CharField(max_length = 20)
    last_name = serializers.CharField(max_length = 50)
    tel = serializers.CharField(max_length = 10)
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserLibrary(**validated_data)
        #hashea contraseña
        user.set_password(password)
        #guarda contraseña hasheada
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style = {'input_type':'password'},write_only= True)
    access_token = serializers.CharField(max_length=200,read_only=True)
    refresh_token = serializers.CharField(max_length=200,read_only=True)
    id = serializers.IntegerField(read_only = True)
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        try:
            user = UserLibrary.objects.get(email__iexact=email)
        except UserLibrary.DoesNotExist:
            raise serializers.ValidationError(
                {"Error":"Credencial no es valida/email"},
                code=status.HTTP_404_NOT_FOUND
            )
        if not user.check_password(password):
            raise serializers.ValidationError(
                {"Error":"Credencial invalida/Password"},
                code=status.HTTP_404_NOT_FOUND
            )
        token = RefreshToken.for_user(user)
        
        return {
            "first_name": str(user.first_name),
            "last_name": str(user.last_name),
            "email": str(user.email),
            "access_token": str(token.access_token),
            "refresh_token":str(token),
        }
    
    
    
    