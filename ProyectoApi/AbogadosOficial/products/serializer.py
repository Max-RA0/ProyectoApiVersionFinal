from rest_framework import serializers
from .models import ServicioLegal, Divorcio, AsesoriaLegal

class ServicioLegalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioLegal
        fields = '__all__'

class DivorcioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divorcio
        fields = '__all__'
        

class AsesoriaLegalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsesoriaLegal
        fields = '__all__'