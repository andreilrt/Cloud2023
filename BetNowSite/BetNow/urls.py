from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", LoginView.as_view(), name='login'),
    path("Registro", views.Registro, name="Registro"),
    path("inicio", views.index_usuario, name="inicio"),
    path("logout", views.logout_view, name="logout"),
    path('consultas_usuario', views.consultas_usuario, name='consultas_usuario'),
    path('realizar_retiro_usuario', views.realizar_retiro_usuario, name='realizar_retiro_usuario'),
    path('edit_data_user', views.edit_data_user, name='edit_data_user'),
    path('agregar_dinero', views.agregar_dinero, name='agregar_dinero'),
    path('registrar_metodo_transaccion', views.registrar_metodo_transaccion, name='registrar_metodo_transaccion'),
    path('realizar_agregar_dinero', views.realizar_agregar_dinero, name='realizar_agregar_dinero'),
    path('realizar_retiro', views.realizar_retiro, name='realizar_retiro'),
    path('deposito', views.deposito, name='deposito'),
    path('retiro', views.retiro, name='retiro'),
    path('ligas', views.Ligas, name='ligas'),
    path('laliga',views.show_matches_laliga, name="laliga"),
    path('premierleague',views.show_matches_premierleague, name="premierleague"),
    path('NBA',views.show_matches_NBA, name="NBA"),
    path('MLB',views.show_matches_MLB, name="MLB"),
]