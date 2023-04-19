from django.http import JsonResponse
from django.shortcuts import render

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
    context = {
        'Avatar': '/static/BetNow/img/Avatar.svg',
        'logo': '/static/BetNow/img/logo.svg',
    }
    return render(request, "BetNow/usuario_inicio.html", context)