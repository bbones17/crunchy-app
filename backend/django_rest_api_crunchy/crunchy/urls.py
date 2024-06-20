from crunchy import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'menues', views.MenuViewSet)
# router.register(r'pedidos', views.PedidoViewSet)

# define the urls
urlpatterns = [
    path('', include(router.urls)),
    path('menues/', views.menues),
    # path('menues/<int:pk>/', views.menu_detail),
    # path('pedidos/', views.pedidos),
    # path('pedidos/<int:pk>/', views.pedido_detail),
    # # path('pedidos/', views.perfiles),
    # path('perfiles/<int:pk>/',views.perfil_detail),


]
