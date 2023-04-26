from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.models import User

# Create your views here.

@user_passes_test(lambda u: not u.is_authenticated, login_url='inicio')
def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            user.backend = 'BetNow.backends.userAuthBackend'
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

@user_passes_test(lambda u: not u.is_authenticated, login_url='inicio')
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

        # Create a new user object with the extracted values
        user = user.objects.create(nombres=nombres, apellidos=apellidos, password=password, pais=pais, ciudad=ciudad, direccion=direccion, email=email, indicativo=indicativo, celular=celular, documento=documento, numero_documento=numero_documento, fecha_expedicion=fecha_expedicion)
        user.save()
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
