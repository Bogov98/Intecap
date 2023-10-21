from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuario
from .models import Curso
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import make_password

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('task:inicio')  # Redirige al index.html después de la autenticación exitosa
    return render(request, 'login.html')

@user_passes_test(lambda u: u.is_superuser)
def inicio(request):
    return render(request, 'index.html')

def curso_view(request):
    cursos = Curso.objects.all()
    return render(request, 'Cursos/cursos.html', {'cursos': cursos})

def create_curso_view(request):
    return render(request, 'Cursos/create_curso.html')


def create_curso(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_curso']
        descripcion = request.POST['descripcion_curso']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']
        duracion = request.POST['duracion']
        horarios = request.POST['horarios']
        establecimiento = request.POST['establecimiento']
        costo = request.POST['costo']
        cupos_disponibles = request.POST['cupos_disponibles']
        estado = True  # Valor predeterminado False si el campo no está presente
        print(estado)
        id_categoria = request.POST['id_categoria']
        curso = Curso(nombre_curso=nombre, descripcion_curso=descripcion,fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,duracion=duracion,horarios=horarios,establecimiento=establecimiento,costo=costo,cupos_disponibles=cupos_disponibles,estado=estado,id_categoria_id=id_categoria)
        curso.save()
        return redirect('task:curso_view')
    return render(request, 'Cursos/create_curso.html')

def editar_curso_view(request,idcurso):
    curso = Curso.objects.get(id_curso=idcurso)
    return render(request, 'Cursos/editar_curso.html',{'curso':curso})

def editar_curso(request,idcurso):
    if request.method == 'POST':
        curso = Curso.objects.get(id_curso=idcurso)
        nombre = request.POST['nombre_curso']
        descripcion = request.POST['descripcion_curso']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']
        duracion = request.POST['duracion']
        horarios = request.POST['horarios']
        establecimiento = request.POST['establecimiento']
        costo = request.POST['costo']
        cupos_disponibles = request.POST['cupos_disponibles']
        estado = True  # Valor predeterminado False si el campo no está presente    
        id_categoria = request.POST['id_categoria']
        curso = Curso(id_curso=idcurso,nombre_curso=nombre, descripcion_curso=descripcion,fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,duracion=duracion,horarios=horarios,establecimiento=establecimiento,costo=costo,cupos_disponibles=cupos_disponibles,estado=estado,id_categoria_id=id_categoria)
        curso.save()
        return redirect('task:curso_view')
    return render(request, 'Cursos/editar_curso.html')

def eliminar_curso(request,idcurso):
    curso = Curso.objects.get(id_curso=idcurso)
    curso.delete()
    return redirect('task:curso_view')