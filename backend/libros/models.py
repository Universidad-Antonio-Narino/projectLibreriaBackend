from django.db import models

# Create your models here.
class Libros(models.Model):
    isbn = models.CharField(max_length=15, null=False, unique=True,primary_key=True)
    titulo = models.CharField(max_length=20,null=False)
    precioCompra = models.IntegerField(null=False)
    precioVenta = models.IntegerField(null=False)
    stock = models.IntegerField(null=False)