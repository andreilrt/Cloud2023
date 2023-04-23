from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", LoginView.as_view(), name='index'),
    path("Registro", views.Registro, name="Registro"),
    path("inicio", views.index_usuario, name="inicio"),
    path("logout", views.logout_view, name="logout")
]