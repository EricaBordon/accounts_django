from django.shortcuts import render, redirect  # render = mostrar HTML, redirect = cambiar de página
from django.contrib.auth import authenticate, login, logout  # funciones de autenticación
from django.contrib.auth.decorators import login_required  # proteger vistas
from django.contrib.auth.models import User  # modelo de usuario de Django


# ---------------- LOGIN ----------------
def login_view(request):
    mensaje = ''

    # Si el usuario envía el formulario
    if request.method == 'POST':
        username = request.POST.get('username')  # obtener usuario
        password = request.POST.get('password')  # obtener contraseña

        # verificar usuario en base de datos
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # iniciar sesión
            return redirect('home')  # redirigir a home
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render(request, 'accounts/login.html', {'mensaje': mensaje})


# ---------------- HOME (PROTEGIDA) ----------------
@login_required  # solo entra si está logueado
def home_view(request):
    return render(request, 'accounts/home.html')


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)  # cerrar sesión
    return redirect('login')  # volver al login


# ---------------- REGISTRO ----------------
def register_view(request):
    mensaje = ''

    # Si el usuario envía el formulario
    if request.method == 'POST':
        username = request.POST.get('username')  # obtener usuario
        password = request.POST.get('password')  # obtener contraseña

        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            mensaje = 'El usuario ya existe'
        else:
            # Crear usuario en la base de datos
            User.objects.create_user(
                username=username,
                password=password
            )
            return redirect('login')  # volver al login después de registrarse

    return render(request, 'accounts/register.html', {'mensaje': mensaje})