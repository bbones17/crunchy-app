from django.shortcuts import render
from rest_framework import permissions, viewsets
from django.contrib.auth.models import  User

# Create your views here.
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for task
from .serializers import MenuSerializer
from .serializers import PedidoSerializer
from .serializers import PerfilSerializer
from .serializers import ReseniaSerializer
from .serializers import IngredienteSerializer
from .serializers import ItemDetallePedidoSerializer
from .serializers import EtiquetaSerializer
from .serializers import PromocionSerializer

from .serializers import UserSerializer

# Menu model
from .models import Menu
from .models import Pedido
from .models import Perfil
from .models import Resenia
from .models import Ingrediente
from .models import ItemDetallePedido
from .models import Etiqueta
from .models import Promocion


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# class PedidoViewSet(viewsets.ModelViewSet):
#     queryset = Pedido.objects.all()
#     serializer_class = PedidoSerializer

# class MenuViewSet(viewsets.ModelViewSet):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer


@csrf_exempt
def menues(request):
    if (request.method == 'GET'):
        # get all the tasks
        menues = Menu.objects.all()
        # serialize the task data
        serializer = MenuSerializer(menues, many=True)
        # return a Json response
        return JsonResponse(serializer.data, safe=False)
    elif (request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = MenuSerializer(data=data)
        # check if the sent information is okay
        if (serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

    # UPDATE


@csrf_exempt
def menu_detail(request, pk):
    try:
        menu = Menu.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    # if (request.method == 'GET'):
    #     menu= Menu.objects.all()
    #     serializer = MenuSerializer(menu,many=False)
    #     return JsonResponse(serializer.data, safe=False)

    if (request.method == 'PUT'):
        data = JSONParser().parse(request)
        serializer = MenuSerializer(menu, data=data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif (request.method == 'DELETE'):
        menu.delete()
        return HttpResponse(status=204)


