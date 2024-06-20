from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=100, null=True)
    descripcion = models.TextField(blank=True, null=True)
    # preferencias


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio_unitario = models.FloatField(max_length=10)
    unidad = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # menues = models.ManyToManyField(Menu,null=True)


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    # menues = models.ManyToManyField(Menu, on_delete=models.DO_NOTHING, null=True)


class Promocion(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    descuento = models.FloatField(max_length=10)
    motivo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    etiquetas_promocion = models.ManyToManyField(Etiqueta)


class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.FloatField(max_length=10, default=0)
    imagen = models.CharField(max_length=100, null=True)
    etiqueta = models.CharField(max_length=30,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ingredientes_menu = models.ManyToManyField(Ingrediente)
    etiquetas_menu = models.ManyToManyField(Etiqueta)


class Resenia(models.Model):
    comentario = models.TextField(blank=True, null=True)
    puntuacion = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    menu_reseniado = models.ForeignKey(
        Menu, on_delete=models.CASCADE, null=False)


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)


class ItemDetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    menu_pedido = models.ForeignKey(Menu, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)


# menu puede estar en varios Pedidos y un pedido tieine multiples menus
