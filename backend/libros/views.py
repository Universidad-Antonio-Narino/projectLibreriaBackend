from django.shortcuts import render
from .models import *
from rest_framework import viewsets,permissions
from rest_framework.views import APIView
from .serializers import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here
class LibrosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CRUD operations on the 'Libro' model.
    """
    queryset = Libro.objects.all() # Retrieves all objects from the 'Libro' table
    permission_classes = [permissions.AllowAny] # Specifies the permission classes for accessing the data
    serializer_class = LibrosSerializers # Specifies the serializer class for serializing and deserializing the data


class TransaccionViewSet(viewsets.ModelViewSet, APIView):
    """
    API endpoint that allows CRUD operations on the 'Transacion' model.
    """
    queryset = Transacion.objects.all() # Retrieves all objects from the 'Transacion' table
    permission_classes = [permissions.AllowAny] # Specifies the permission classes for accessing the data
    serializer_class = TransaccionesSerializers # Specifies the serializer class for serializing and deserializing the data

    @receiver(post_save, sender=Transacion) #recibe el tipo de envio para el caso de que llame transaccion
    def actualizar_stock_libros(sender, instance, **kwargs):
        """
        Signal receiver function that updates the stock of a book based on the type of transaction.
        """
        libro = instance.libro # Retrieves the book associated with the transaction
        if instance.tipo_transaccion.upper() == 'ABASTECIMIENTO':
            libro.stock += instance.cantidad_ejemplares # Increases the stock if it's a supply transaction
        elif instance.tipo_transaccion.upper() == 'VENTA':
            libro.stock -= instance.cantidad_ejemplares # Decreases the stock if it's a sale transaction
        libro.save() # Saves the updated stock

    
