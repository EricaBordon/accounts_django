from django.shortcuts import render, redirect  # redirect permite cambiar de página
from django.contrib.auth import authenticate, login, logout  # funciones de Django
from django.contrib.auth.decorators import login_required

def login_view(request):
    mensaje = ''

    # Si el usuario envía el formulario
    if request.method == 'POST':
        username = request.POST.get('username')  # obtener usuario
        password = request.POST.get('password')  # obtener contraseña

        # verificar en base de datos
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # iniciar sesión
            return redirect('home')  # 🔥 redirige a otra vista
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render(request, 'accounts/login.html', {'mensaje': mensaje})


# Vista después del login
def home_view(request):
    return render(request, 'accounts/home.html')


# Vista para cerrar sesión
def logout_view(request):
    logout(request)  # cerrar sesión
    return redirect('login')  # vuelve al login

@login_required
def home_view(request):
    return render(request, 'accounts/home.html')