from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    indicativo = models.CharField(max_length=10)
    celular = models.CharField(max_length=20, unique=True)
    documento = models.CharField(max_length=50)
    numero_documento = models.CharField(max_length=50, unique=True)
    fecha_expedicion = models.DateField()

    def __str__(self):
        return self.email


class Banco(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    nombre_titular = models.CharField(max_length=100)
    numero_cuenta = models.CharField(max_length=20)
    tipo_cuenta = models.CharField(max_length=20)
    nombre_banco = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_banco


class PSE(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    banco = models.CharField(max_length=100)
    tipo_cuenta = models.CharField(max_length=50)
    tipo_documento = models.CharField(max_length=50)
    numero_documento = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField()

    def __str__(self):
        return self.banco


class Tarjeta(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    nombre_titular = models.CharField(max_length=100)
    numero_tarjeta = models.CharField(max_length=16)
    fecha_expiracion = models.DateField()
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return self.nombre_titular

