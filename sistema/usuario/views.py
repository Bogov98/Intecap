from django.contrib.auth import authenticate, login as auth_login  # Cambiamos el nombre de la función de autenticación
from django.shortcuts import render
from django.shortcuts import redirect


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)  # Autenticación exitosa, utilizamos auth_login
            return redirect('inicio')  # Redirige al index.html después de la autenticación exitosa
    # Si la autenticación falla o es una solicitud GET, renderiza el formulario de inicio de sesión.
    return render(request, 'login.html')


def inicio(request):
    return render(request, 'index.html')

