from django.shortcuts import render
from .models import *
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from .serializers import *
from django.db.models.signals import post_save
from django.dispatch import receiver

# ViewSet para la administración de libros
class LibrosAdminViewSet(viewsets.ModelViewSet):
    queryset = LibroAdmin.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LibrosAdminSerializers

# ViewSet para la administración de transacciones
class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TransaccionesSerializers

    # Señal para actualizar el stock de libros después de guardar una transacción
    @receiver(post_save, sender=Transacion)
    def actualizar_stock_libros(sender, instance, **kwargs):
        libro = instance.libro
        if instance.tipo_transaccion.upper() == 'ABASTECIMIENTO':
            libro.stock += instance.cantidad_ejemplares
        elif instance.tipo_transaccion.upper() == 'VENTA':
            libro.stock -= instance.cantidad_ejemplares
        libro.save()
