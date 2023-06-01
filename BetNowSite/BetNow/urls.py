from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", LoginView.as_view(), name='index'),
    path("Registro", views.Registro, name="Registro"),
    path("inicio", views.index_usuario, name="inicio"),
    path("logout", views.logout_view, name="logout"),
    path('consultas_usuario/<str:first_name>', views.consultas_usuario, name='consultas_usuario'),
    path('realizar_retiro_usuario/<str:first_name>', views.realizar_retiro_usuario, name='realizar_retiro_usuario')
]