from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Perfil

# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        perfil = authenticate(request, email=email, password=password)
        if perfil is not None:
            login(request, perfil)
            perfil.backend = 'BetNow.backends.PerfilAuthBackend'
            return redirect('inicio')
        else:
            error_message = "Email o contraseña invalidos, por favor intente de nuevo."
            context = {
                'error_message': error_message,
                'logo': '/static/BetNow/img/logo.svg',
                'Bet_Inicio': '/static/BetNow/img/Bet_Inicio.svg',
                'Basketball': '/static/BetNow/img/Basketball.svg',
                'Fondo': '/static/BetNow/img/Basketball.svg',
                'Futbol': '/static/BetNow/img/Futbol.svg',
                'Tennis': '/static/BetNow/img/Tennis.svg',
            }
            return render(request, 'BetNow/index.html', context)
    else:
        context = {
            'logo': '/static/BetNow/img/logo.svg',
            'Bet_Inicio': '/static/BetNow/img/Bet_Inicio.svg',
            'Basketball': '/static/BetNow/img/Basketball.svg',
            'Fondo': '/static/BetNow/img/Basketball.svg',
            'Futbol': '/static/BetNow/img/Futbol.svg',
            'Tennis': '/static/BetNow/img/Tennis.svg',
        }
        return render(request, "BetNow/index.html", context)

def Registro(request):
    if request.method == 'POST':
        # Extract the values of the form fields from the request.POST dictionary
        nombres = request.POST['first-name']
        apellidos = request.POST['last-name']
        password = request.POST['password']
        pais = request.POST['country']
        ciudad = request.POST['city']
        direccion = request.POST['address']
        email = request.POST['email']
        indicativo = request.POST['phone-prefix']
        celular = request.POST['phone']
        documento = request.POST['document-type']
        numero_documento = request.POST['document-number']
        fecha_expedicion = request.POST['issue-date']

        # Create a new Perfil object with the extracted values
        perfil = Perfil.objects.create(nombres=nombres, apellidos=apellidos, password=password, pais=pais, ciudad=ciudad, direccion=direccion, email=email, indicativo=indicativo, celular=celular, documento=documento, numero_documento=numero_documento, fecha_expedicion=fecha_expedicion)
        perfil.save()
        context = {
            'logo': '/static/BetNow/img/logo.svg',
            'Bet_Inicio': '/static/BetNow/img/Bet_Inicio.svg',
            'Basketball': '/static/BetNow/img/Basketball.svg',
            'Fondo': '/static/BetNow/img/Basketball.svg',
            'Futbol': '/static/BetNow/img/Futbol.svg',
            'Tennis': '/static/BetNow/img/Tennis.svg',
            'Avatar': '/static/BetNow/img/Avatar.svg'
        }
        return redirect("inicio")
    else:
        context = {
            'logo': '/static/BetNow/img/logo.svg',
        }
        return render(request,"BetNow/signup.html", context)

@login_required
def index_usuario(request):
    context = {
        'logo': '/static/BetNow/img/logo.svg',
        'Bet_Inicio': '/static/BetNow/img/Bet_Inicio.svg',
        'Basketball': '/static/BetNow/img/Basketball.svg',
        'Fondo': '/static/BetNow/img/Basketball.svg',
        'Futbol': '/static/BetNow/img/Futbol.svg',
        'Tennis': '/static/BetNow/img/Tennis.svg',
        'Avatar': '/static/BetNow/img/Avatar.svg'
    }
    return render(request, "BetNow/usuario_inicio.html", context)

def logout_view(request):
    logout(request)
    return redirect('index')
