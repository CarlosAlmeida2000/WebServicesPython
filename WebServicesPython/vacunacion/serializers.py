from rest_framework import serializers
from vacunacion.models import *

class CiudadanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciudadanos
        fields = '__all__'