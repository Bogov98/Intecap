from usuario.models import Usuario
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__' #definimos todos lo valores del modelo, pero se pueden definir los campos que queremos
        