from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import Perfil, Banco, PSE, Tarjeta
from django.contrib.auth.models import User

# Create your views here.

@user_passes_test(lambda u: not u.is_authenticated, login_url='inicio')
def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
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
        user = User.objects.create_user(username=email, password=password, first_name=nombres, last_name=apellidos, email=email)

        # Associate the user with the perfil
        perfil = Perfil.objects.create(user=user, pais=pais, ciudad=ciudad, direccion=direccion, email=email, indicativo=indicativo, celular=celular, documento=documento, numero_documento=numero_documento, fecha_expedicion=fecha_expedicion)
        
        user.save()
        perfil.save()

        # Check the selected payment method and save the corresponding information
        payment_method = request.POST.get('payment-method')

        if payment_method == 'banks':
            if 'colombian-banks' in request.POST:
                # Process bank information
                banco_nombre = request.POST['colombian-banks']
                titular = request.POST['account-name']
                numero_cuenta = request.POST['account-number']
                tipo_cuenta = request.POST['account-type']
                banco = Banco.objects.create(perfil=perfil, nombre_titular=titular, numero_cuenta=numero_cuenta, tipo_cuenta=tipo_cuenta, nombre_banco=banco_nombre)
                banco.save()

        elif payment_method == 'pse':
            if 'pse-bank' in request.POST:
                # Process PSE information
                banco = request.POST['pse-bank']
                tipo_cuenta = request.POST['pse-account-type']
                tipo_documento = request.POST['pse-document-type']
                numero_documento = request.POST['pse-document-number']
                nombre = request.POST['pse-first-name']
                apellido = request.POST['pse-last-name']
                correo_electronico = request.POST['pse-email']
                pse = PSE.objects.create(perfil=perfil, banco=banco, tipo_cuenta=tipo_cuenta, tipo_documento=tipo_documento, numero_documento=numero_documento, nombre=nombre, apellido=apellido, correo_electronico=correo_electronico)
                pse.save()

        elif payment_method == 'card':
            if 'cardholder-name' in request.POST:
                # Process card information
                nombre_titular = request.POST['cardholder-name']
                numero_tarjeta = request.POST['card-number']
                fecha_expiracion = request.POST['month'] + '/' + request.POST['year']
                cvv = request.POST['cvv']
                tarjeta = Tarjeta.objects.create(perfil=perfil, nombre_titular=nombre_titular, numero_tarjeta=numero_tarjeta, fecha_expiracion=fecha_expiracion, cvv=cvv)
                tarjeta.save()

        context = {
            'logo': '/static/BetNow/img/logo.svg',
            'Bet_Inicio': '/static/BetNow/img/Bet_Inicio.svg',
            'Basketball': '/static/BetNow/img/Basketball.svg',
            'Fondo': '/static/BetNow/img/Basketball.svg',
            'Futbol': '/static/BetNow/img/Futbol.svg',
            'Tennis': '/static/BetNow/img/Tennis.svg',
            'Avatar': '/static/BetNow/img/Avatar.svg'
        }

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            error_message = "Email o contraseña inválidos, por favor intente de nuevo."
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

@login_required
def consultas_usuario(request, first_name):
    context = {
        'logo': '/static/BetNow/img/logo.svg',
        'Bet_Inicio': '/static/BetNow/img/Bet_Inicio.svg',
        'Basketball': '/static/BetNow/img/Basketball.svg',
        'Fondo': '/static/BetNow/img/Basketball.svg',
        'Futbol': '/static/BetNow/img/Futbol.svg',
        'Tennis': '/static/BetNow/img/Tennis.svg',
        'Avatar': '/static/BetNow/img/Avatar.svg',
        'ATM': '/static/BetNow/img/atm.svg',
        'first_name': first_name
    }
    return render(request, "BetNow/consultas_usuario.html", context)

@login_required
def realizar_retiro_usuario(request, first_name):
    context = {
        'logo': '/static/BetNow/img/logo.svg',
        'Bet_Inicio': '/static/BetNow/img/Bet_Inicio.svg',
        'Basketball': '/static/BetNow/img/Basketball.svg',
        'Fondo': '/static/BetNow/img/Basketball.svg',
        'Futbol': '/static/BetNow/img/Futbol.svg',
        'Tennis': '/static/BetNow/img/Tennis.svg',
        'Avatar': '/static/BetNow/img/Avatar.svg',
        'ATM': '/static/BetNow/img/atm.svg',
        'first_name': first_name
    }
    return render(request, "BetNow/realizar_retiro_usuario.html", context)

def logout_view(request):
    logout(request)
    return redirect('index')
