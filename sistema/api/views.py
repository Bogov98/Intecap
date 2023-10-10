from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from api.serializers import UserSerializer
from usuario.models import Usuario



# Create your views here.

# Extender el schema nos permite manipular OPEN API con lo que trabaja spectacular
# Nos permite hacer cambios.
@extend_schema_view(
    list =extend_schema(description='permite obtener lista usuarios'),
    retrieve = extend_schema(description='permite obtener un usuario'),
    create = extend_schema(description='permite crear un usuario'),
    update = extend_schema(description='permite actualizar un usuario'),
    destroy = extend_schema(description='permite eliminar un usuario'),
)

# Definimos nuestra clase, viewset nos permite trabajar con modelos, hace los dif.metodos
# GET, POST, PUT, DELETE = List, retrieve, update, destroy
class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    #lookup_field = 'id' #esto es para que cuando se haga una peticion se pueda buscar por id
    #lookup_url_kwarg = 'id' #esto es para que cuando se haga una peticion se pueda buscar por id
