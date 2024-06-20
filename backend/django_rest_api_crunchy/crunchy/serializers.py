from rest_framework import routers,serializers,viewsets
from django.contrib.auth.models import  User
from .models import Menu
from .models import Pedido
from .models import Etiqueta
from .models import Promocion
from .models import Resenia
from .models import Ingrediente
from .models import Perfil

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','nombre', 'descripcion', 'precio','imagen','etiqueta', 'created_at']
        depth=1

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ['cantidad', 'menues_pedidos',  'created_at']

class EtiquetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Etiqueta
        fields = ['nombre', 'descripcion', 'precio','imagen', 'created_at']

class PromocionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promocion
        fields = ['nombre', 'descripcion', 'precio','imagen', 'created_at']

class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'descripcion', 'precio','imagen', 'created_at']

class ReseniaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resenia
        fields = ['nombre', 'descripcion', 'precio','imagen', 'created_at']

class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfil
        fields = ['usuario', 'imagen', 'descripcion',]

class ItemDetallePedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'descripcion', 'precio','imagen', 'created_at']
