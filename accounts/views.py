from django.shortcuts import render

def login_view(request):
    mensaje = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == '1234':
            mensaje = 'Login correcto'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render(request, 'accounts/login.html', {'mensaje': mensaje})