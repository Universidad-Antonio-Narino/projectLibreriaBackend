from django.db import models

# Create your models here.
"""
Model definitions
"""
class User(models.Model):
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
