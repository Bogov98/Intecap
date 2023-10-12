from django.contrib.auth import authenticate, login as auth_login  # Cambiamos el nombre de la función de autenticación
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required




def login_view(request):
    if request.method == 'POST':
        # Obtén los datos de inicio de sesión del formulario
        email = request.POST['email']
        password = request.POST['password']

        # Autentica al usuario utilizando las credenciales proporcionadas
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Si el usuario es autenticado con éxito, inicia la sesión
            auth_login(request, user)
           # request.session['user_name'] = user.get_full_name()
            return redirect('inicio')  # Cambia a la página principal después del inicio de sesión
        else:
            # Si la autenticación falla, muestra un mensaje de error
            error_message = "Credenciales inválidas. Inténtalo de nuevo."
            messages.error(request, error_message)
            return render(request, 'login.html')

    # Si la solicitud es GET, simplemente muestra el formulario de inicio de sesión
    return render(request, 'login.html')




@login_required
def inicio(request):
    return render(request, 'index.html')
