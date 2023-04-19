from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Registro", views.Registro, name="Registro"),
    path("Usuario", views.usuario_inicio, name="Usuario"),
]