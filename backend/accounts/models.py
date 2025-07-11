from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.utils import timezone
# Create your models here.
"""
Model definitions
"""
"""class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True,null=False)
    saldo = models.BigIntegerField(default = 0)
    nombre =models.CharField(max_length=50,null=False)
    numeroTelefono = models.CharField(max_length=10,null=False)
    cedula = models.CharField(max_length=50,null=False,unique=True,default='')
    password = models.CharField(max_length=16,null=False)
    ifLogged = models.BooleanField(default=False)

    def __str__(self):
        return "{} -{}".format(self.nombre, self.email)
"""

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, first_name=None, last_name=None, username=None,cedula=None):
        """
        Verificar si el campo de correo es vacio, si no esta 
        la funcion raise levanta un error
        """
        if not email:
            raise ValueError("El email es obligatorio")
        if not cedula:
            raise ValueError("La cedula es obligatoria")
        # convierte el email a un formato estándar, por ejemplo, lo transforma a minúsculas.
        user = self.model(email=self.normalize_email(
            email), first_name=first_name, last_name=last_name, username=username,cedula=cedula)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name=None, last_name=None, username=None,cedula=None):
        if not password:
            raise ValueError("La contraseña es obligatoria")

        user = self.create_user(
            email, password, first_name, last_name, username=username,cedula=cedula)
        user.save()

        # permisos
        # si creo un superusuario tendra estos permisos
        user.is_superuser = True  # es superusuario ?
        user.is_staff = True  # es empleado?
        user.is_verified = True  # esta autenticado o verificado ?
        user.is_approved = True  # esta aprovado?
        user.save()  # guardar los permisos
        return user


#usando las clases de django
class UserLibrary(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True,null=False)
    saldo = models.BigIntegerField(default=0)
    tel = models.CharField(max_length=10,null=False,unique=True)
    cedula = models.CharField(primary_key=True,unique=True,max_length=100,default="")
    username = models.CharField(max_length=150,unique=True)
    #permissions
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','cedula']

