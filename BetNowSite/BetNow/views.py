from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BancoForm, PSEForm, TarjetaForm
from .models import Perfil, Banco, PSE, Tarjeta, Deposito
from django.contrib.auth.models import User
from decimal import Decimal


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
def consultas_usuario(request):
    context = {
        'logo': '/static/BetNow/img/logo.svg',
        'Bet_Inicio': '/static/BetNow/img/Bet_Inicio.svg',
        'Basketball': '/static/BetNow/img/Basketball.svg',
        'Fondo': '/static/BetNow/img/Basketball.svg',
        'Futbol': '/static/BetNow/img/Futbol.svg',
        'Tennis': '/static/BetNow/img/Tennis.svg',
        'Avatar': '/static/BetNow/img/Avatar.svg',
        'ATM': '/static/BetNow/img/atm.svg',
        'saldo': request.user.perfil.saldo,  # Agrega el saldo actual del usuario al contexto
    }
    return render(request, "BetNow/consultas_usuario.html", context)


@login_required
def realizar_retiro_usuario(request):
    perfil = Perfil.objects.get(user=request.user)
    bancos = perfil.banco_set.all()
    tarjetas = perfil.tarjeta_set.all()
    pses = perfil.pse_set.all()

    context = {
        'logo': '/static/BetNow/img/logo.svg',
        'Bet_Inicio': '/static/BetNow/img/Bet_Inicio.svg',
        'Basketball': '/static/BetNow/img/Basketball.svg',
        'Fondo': '/static/BetNow/img/Basketball.svg',
        'Futbol': '/static/BetNow/img/Futbol.svg',
        'Tennis': '/static/BetNow/img/Tennis.svg',
        'Avatar': '/static/BetNow/img/Avatar.svg',
        'ATM': '/static/BetNow/img/atm.svg',
        'bancos': bancos,
        'tarjetas': tarjetas,
        'pses': pses
    }
    return render(request, "BetNow/realizar_retiro_usuario.html", context)

@login_required
def realizar_retiro(request):
    if request.method == 'POST':
        cantidad = Decimal(request.POST.get('cantidad'))  # Convertir a Decimal
        metodo_transaccion = request.POST.get('metodo-transaccion')

        perfil = request.user.perfil
        if cantidad <= perfil.saldo:
            # Restar la cantidad del saldo
            perfil.saldo -= cantidad
            perfil.save()

            # Realizar las operaciones correspondientes según el método de transacción seleccionado
            if metodo_transaccion.startswith('bank-'):
                # Realizar operaciones para método de banco
                # ...
                return redirect('realizar_retiro_usuario')
            elif metodo_transaccion.startswith('pse-'):
                # Realizar operaciones para método PSE
                # ...
                return redirect('realizar_retiro_usuario')

        else:
            # Mostrar mensaje de advertencia si la cantidad a retirar es mayor al saldo disponible
            messages.warning(request, 'La cantidad a retirar es mayor al saldo disponible.')

    return redirect('realizar_retiro_usuario')

@login_required
def edit_data_user(request):
    context = {
        'logo': '/static/BetNow/img/logo.svg',
        'Bet_Inicio': '/static/BetNow/img/Bet_Inicio.svg',
        'Basketball': '/static/BetNow/img/Basketball.svg',
        'Fondo': '/static/BetNow/img/Basketball.svg',
        'Futbol': '/static/BetNow/img/Futbol.svg',
        'Tennis': '/static/BetNow/img/Tennis.svg',
        'Avatar': '/static/BetNow/img/Avatar.svg',
        'ATM': '/static/BetNow/img/atm.svg'
    }
    return render(request, "BetNow/edit_data_user.html", context)

@login_required
def agregar_dinero(request):
    user = request.user
    saldo_actual = user.perfil.saldo  # Obtener el saldo actual del usuario
    context = {
        'logo': '/static/BetNow/img/logo.svg',
        'Bet_Inicio': '/static/BetNow/img/Bet_Inicio.svg',
        'Basketball': '/static/BetNow/img/Basketball.svg',
        'Fondo': '/static/BetNow/img/Basketball.svg',
        'Futbol': '/static/BetNow/img/Futbol.svg',
        'Tennis': '/static/BetNow/img/Tennis.svg',
        'Avatar': '/static/BetNow/img/Avatar.svg',
        'ATM': '/static/BetNow/img/atm.svg',
        'user': user,
        'saldo_actual': saldo_actual,
    }
    return render(request, "BetNow/agregar_dinero.html", context)

@login_required
def realizar_agregar_dinero(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        cantidad = Decimal(request.POST.get('cantidad'))
        metodo_transaccion = request.POST.get('metodo-transaccion')

        # Realizar las operaciones necesarias, como actualizar el saldo del usuario y crear un registro de depósito
        user = request.user
        perfil = user.perfil

        # Actualizar el saldo del usuario
        perfil.saldo += cantidad
        perfil.save()

        # Registrar el depósito en el historial
        deposito = Deposito.objects.create(perfil=perfil, cantidad=cantidad)
        deposito.save()
        # Redirigir a la página agregar_dinero.html después de procesar el formulario
        return redirect('agregar_dinero')

@login_required
def registrar_metodo_transaccion(request):
    banks_form = BancoForm()
    pse_form = PSEForm()
    card_form = TarjetaForm()
    payment_method = None

     # Check the selected payment method and save the corresponding information
    payment_method = request.POST.get('payment-method')
    perfil = request.user.perfil
    if payment_method == 'banks':
        if 'colombian-banks' in request.POST:
            # Process bank information
            banco_nombre = request.POST['colombian-banks']
            titular = request.POST['account-name']
            numero_cuenta = request.POST['account-number']
            tipo_cuenta = request.POST['account-type']
            banco = Banco.objects.create(perfil=perfil, nombre_titular=titular, numero_cuenta=numero_cuenta, tipo_cuenta=tipo_cuenta, nombre_banco=banco_nombre)
            banco.save()
            return redirect('inicio')

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
            return redirect('inicio')

    elif payment_method == 'card':
        if 'cardholder-name' in request.POST:
            # Process card information
            nombre_titular = request.POST['cardholder-name']
            numero_tarjeta = request.POST['card-number']
            fecha_expiracion = request.POST['month'] + '/' + request.POST['year']
            cvv = request.POST['cvv']
            tarjeta = Tarjeta.objects.create(perfil=perfil, nombre_titular=nombre_titular, numero_tarjeta=numero_tarjeta, fecha_expiracion=fecha_expiracion, cvv=cvv)
            tarjeta.save()
            return redirect('inicio')


    context = {
        'logo': '/static/BetNow/img/logo.svg',
        'Bet_Inicio': '/static/BetNow/img/Bet_Inicio.svg',
        'Basketball': '/static/BetNow/img/Basketball.svg',
        'Fondo': '/static/BetNow/img/Basketball.svg',
        'Futbol': '/static/BetNow/img/Futbol.svg',
        'Tennis': '/static/BetNow/img/Tennis.svg',
        'Avatar': '/static/BetNow/img/Avatar.svg',
        'banks_form': banks_form,
        'pse_form': pse_form,
        'card_form': card_form
    }

    return render(request, 'BetNow/registrar_metodo_transaccion.html', context)


@login_required
def deposito(request):
    depositos = Deposito.objects.filter(perfil=request.user.perfil)
    context = {
        'logo': '/static/BetNow/img/logo.svg',
        'Bet_Inicio': '/static/BetNow/img/Bet_Inicio.svg',
        'Basketball': '/static/BetNow/img/Basketball.svg',
        'Fondo': '/static/BetNow/img/Basketball.svg',
        'Futbol': '/static/BetNow/img/Futbol.svg',
        'Tennis': '/static/BetNow/img/Tennis.svg',
        'Avatar': '/static/BetNow/img/Avatar.svg',
        'depositos': depositos,
    }
    return render(request, "BetNow/deposito.html", context)

@login_required
def retiro(request):
    retiros = Retiro.objects.filter(perfil=request.user.perfil)
    context = {
        'logo': '/static/BetNow/img/logo.svg',
        'Bet_Inicio': '/static/BetNow/img/Bet_Inicio.svg',
        'Basketball': '/static/BetNow/img/Basketball.svg',
        'Fondo': '/static/BetNow/img/Basketball.svg',
        'Futbol': '/static/BetNow/img/Futbol.svg',
        'Tennis': '/static/BetNow/img/Tennis.svg',
        'Avatar': '/static/BetNow/img/Avatar.svg',
        'depositos': retiros,
    }
    return render(request, "BetNow/deposito.html", context)


def logout_view(request):
    logout(request)
    return redirect('index')
