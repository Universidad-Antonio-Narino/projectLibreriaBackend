from rest_framework import serializers
from .models import *

#convierte el modelo en datos que pueden ser consultados
class LibrosAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = LibroAdmin
        fields = '__all__'
        #marca el campo el cual no se podra modificar
        #read_only_fields = ('created_at')


class LibrosUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = LibroUser
        fields = '__all__'



class TransaccionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transacion
        fields = '__all__'

        
