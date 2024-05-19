from django.db import models

class Transacion(models.Model):
    """
    Model representing a transaction.
    """
    id = models.AutoField(primary_key=True)
    tipo_transaccion = models.CharField(max_length=15,null=False)
    fecha_realizacion = models.DateTimeField(auto_now_add=True)
    cantidad_ejemplares = models.IntegerField(null=False)

    class Meta:
        verbose_name_plural = "Transaccion"
class Libro(models.Model):
    """
    Model representing a book.
    """
    isbn = models.CharField(max_length=15, null=False, unique=True, primary_key=True)
    titulo = models.CharField(max_length=20, null=False)
    precioCompra = models.IntegerField(null=False)
    precioVenta = models.IntegerField(null=False)
    stock = models.IntegerField(null=False)
    transaccion = models.ForeignKey(Transacion, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Libro"

    

