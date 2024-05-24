from django.db.models import Q #para construir consultas complejas en Django
from rest_framework import serializers
from rest_framework.validators import UniqueValidator 
"""es una clase que se utiliza en los serializadores de DRF para validar que un campo sea único en un conjunto de objetos"""
from .models import User
from django.core.exceptions import ValidationError
"""Esta importación trae la excepción ValidationError de Django, que se puede utilizar para indicar que ha ocurrido un error de validación en algún punto de tu código."""
from uuid import uuid4 
"""es una función que genera un identificador único universal (UUID) de forma aleatoria."""

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True, validators = [UniqueValidator(queryset=User.objects.all())])#valida que no existan correos iguales
    username = serializers.CharField(required = True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(max_length = 16)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'admin',
            'nombre',
            'numeroTelefono',
        )

class UserLoginSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(required=False,read_only=True)

    def validar(self,data):
        user_id = data.get("user_id",None)
        password = data.get("password",None)
        if not user_id and not password:
            raise ValidationError("algun dato no ha sido ingresado")
        user = None

        #validador de correo
        if '@' in user_id:
            user = User.objects.filter(
                Q(email = user_id) & Q(password = password)
            ).distinct()
            if not user.exists():
                raise ValidationError('Las credenciales no son correctas')
            user = User.objects.get(email = user_id)
        else:
            user = User.objects.filter(
                Q(username = user_id) & 
                Q(password = password)
            ).distinct()
            if not user.exists():
                raise ValidationError('las credenciales son incorrectas')
            user = User.objects.get(username = user_id)
            if user.ifLogged:
                raise ValidationError("El usuario ya esta logeado")
            user.ifLogged = True
            data['token'] = uuid4()#creacion de token
            user.token = data['token']
            user.save()
            return data
    class Meta:
        model = User
        fields = (
            'user_id',
            'password',
            'token',
        )
        read_only_fields = (
            'token',
        )