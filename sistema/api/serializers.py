from usuario.models import Usuario
from aplicacion.models import Estudiante

from aplicacion.models import Estudiante,CategoriaCurso, Curso
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__' #definimos todos lo valores del modelo, pero se pueden definir los campos que queremos
        
class CategoriaCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaCurso
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__' 