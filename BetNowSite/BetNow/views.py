from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Perfil

# Create your views here.
def index(request):
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
    context = {
        'logo': '/static/BetNow/img/logo.svg',
    }
    return render(request,"BetNow/signup.html", context)

def usuario_inicio(request):
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

        # Redirect to the success page
        return redirect('BetNow/usuario_inicio.html')
    context = {
        'Bet_Inicio': '/static/BetNow/img/Bet_Inicio.svg',
        'Basketball': '/static/BetNow/img/Basketball.svg',
        'Fondo': '/static/BetNow/img/Basketball.svg',
        'Futbol': '/static/BetNow/img/Futbol.svg',
        'Tennis': '/static/BetNow/img/Tennis.svg',
        'Avatar': '/static/BetNow/img/Avatar.svg',
        'logo': '/static/BetNow/img/logo.svg',
    }
    return render(request, "BetNow/Registro.html", context)