from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'logo': '/static/BetNow/logo.svg',
        'Bet_Inicio': '/static/BetNow/Bet_Inicio.svg',
        'Basketball': '/static/BetNow/Basketball.svg',
        'Fondo': '/static/BetNow/Basketball.svg',
        'Futbol': '/static/BetNow/Futbol.svg',
        'Tennis': '/static/BetNow/Tennis.svg',
    }
    return render(request, "BetNow/index.html", context)

def Registro(request):
    context = {
        'logo': '/static/BetNow/logo.svg',
    }
    return render(request,"BetNow/signup.html", context)