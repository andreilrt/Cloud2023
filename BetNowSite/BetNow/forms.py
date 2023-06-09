from django import forms
from .models import Banco, PSE, Tarjeta

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['nombre_titular', 'numero_cuenta', 'tipo_cuenta', 'nombre_banco']

class PSEForm(forms.ModelForm):
    class Meta:
        model = PSE
        fields = ['banco', 'tipo_cuenta', 'tipo_documento', 'numero_documento', 'nombre', 'apellido', 'correo_electronico']

class TarjetaForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ['nombre_titular', 'numero_tarjeta', 'fecha_expiracion', 'cvv']
