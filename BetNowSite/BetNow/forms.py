from django import forms
from .models import Banco, PSE, Tarjeta

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['perfil', 'nombre_titular', 'numero_cuenta', 'tipo_cuenta', 'nombre_banco']
        labels = {
            'nombre_titular': 'Nombre del titular',
            'numero_cuenta': 'Número de cuenta',
            'tipo_cuenta': 'Tipo de cuenta',
            'nombre_banco': 'Nombre del banco'
        }

class PSEForm(forms.ModelForm):
    class Meta:
        model = PSE
        fields = ['perfil', 'banco', 'tipo_cuenta', 'tipo_documento', 'numero_documento', 'nombre', 'apellido', 'correo_electronico']
        labels = {
            'banco': 'Banco',
            'tipo_cuenta': 'Tipo de cuenta',
            'tipo_documento': 'Tipo de documento',
            'numero_documento': 'Número de documento',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo_electronico': 'Correo electrónico'
        }

class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ['perfil', 'nombre_titular', 'numero_tarjeta', 'fecha_expiracion', 'cvv']
        labels = {
            'nombre_titular': 'Nombre del titular',
            'numero_tarjeta': 'Número de tarjeta',
            'fecha_expiracion': 'Fecha de expiración (MM/YY)',
            'cvv': 'CVV'
        }
