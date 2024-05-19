from django.shortcuts import render
from .models import *
from rest_framework import viewsets,permissions
from .serializers import LibrosSerializers

# Create your views here.
class LibrosViewSet(viewsets.ModelViewSet):
    abastecimiento = Libro.objects.
    queryset = Libro.objects.all()#me consulta todos los objetos de la tabla
    permission_classes = [permissions.AllowAny]#verifica quien puede acceder a los datos, autenticacion
    #en allowAny todos pueden acceder
    serializer_class = LibrosSerializers


#class 