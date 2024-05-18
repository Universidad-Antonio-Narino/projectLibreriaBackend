from rest_framework import serializers
from .models import Libros

#convierte el modelo en datos que pueden ser consultados
class LibrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = '__all__'
        #marca el campo el cual no se podra modificar
        #read_only_fields = ('created_at')