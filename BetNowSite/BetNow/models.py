from django.db import models

class Perfil(models.Model):
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
