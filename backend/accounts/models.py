from django.db import models

# Create your models here.

"""
Model definitions
"""
class User(models.Model):
    email = models.EmailField(unique=True,null=False)
    admin = models.BooleanField(default=False)
    nombre =models.CharField(max_length=50,null=False)
    numeroTelefono = models.CharField(max_length=10,null=False)
    password = models.CharField(max_length=16,null=False)
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")

    def __str__(self):
        return "{} -{}".format(self.username, self.email)