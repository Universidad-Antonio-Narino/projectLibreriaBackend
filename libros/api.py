from .models import Libros
from rest_framework import viewsets,permissions
from .serializers import LibrosSerializers
class LibrosViewSet(viewsets.ModelViewSet):
    queryset = Libros.objects.all()#me consulta todos los objetos de la tabla
    permission_classes = [permissions.AllowAny]#verifica quien puede acceder a los datos, autenticacion
    #en allowAny todos pueden acceder
    serializer_class = LibrosSerializers