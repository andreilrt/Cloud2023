from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    indicativo = models.CharField(max_length=10)
    celular = models.CharField(max_length=20)
    documento = models.CharField(max_length=50)
    numero_documento = models.CharField(max_length=50)
    fecha_expedicion = models.DateField()

    def __str__(self):
        return self.nombres + ' ' + self.apellidos
