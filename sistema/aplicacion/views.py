from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuario
from .models import CategoriaCurso
from .models import Curso
from .models import Estudiante
from .models import Inscripcion
from .models import Notificacion
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('task:inicio')  # Redirige al index.html después de la autenticación exitosa
    return render(request, 'login.html')

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def inicio(request):
    return render(request, 'index.html')

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def inicio(request):
    return render(request, 'index.html')

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def curso_view(request):
    cursos = Curso.objects.all()
    return render(request, 'Cursos/cursos.html', {'cursos': cursos})

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def create_curso_view(request):
    return render(request, 'Cursos/create_curso.html')

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
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

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def editar_curso_view(request,idcurso):
    curso = Curso.objects.get(id_curso=idcurso)
    return render(request, 'Cursos/editar_curso.html',{'curso':curso})

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
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

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def eliminar_curso(request,idcurso):
    curso = Curso.objects.get(id_curso=idcurso)
    curso.delete()
    return redirect('task:curso_view')

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def search_categoria(request):
    search_term = request.GET.get('search')
    categorias = CategoriaCurso.objects.filter(Q(nombre_categoria__icontains=search_term))
    user_list = [{'id': categoria.id_categoria, 'text': categoria.nombre_categoria} for categoria in categorias]
    return JsonResponse(user_list, safe=False)


def formulario_view(request,idcurso):
    curso = Curso.objects.get(id_curso=idcurso)
    return render(request, 'Formulario/formulario.html',{'curso':curso})



def enviar_formulario(request,idcurso):
    if request.method == 'POST':
        dpi = request.POST['dpi']
        nombre = request.POST['nombre']
        genero = request.POST['genero']
        escolaridad = request.POST['escolaridad']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        etnia = request.POST['etnia']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        edad = request.POST['edad']
        estudiante = Estudiante(
            dpi=dpi,
            genero=genero,
            escolaridad=escolaridad,
            telefono=telefono,
            direccion=direccion,
            etnia=etnia,
            fecha_nacimiento=fecha_nacimiento,
            edad=edad,
            id_curso_id=idcurso,
        )
        estudiante.save()
        estudiante2=Estudiante.objects.get(dpi=dpi)
        fecha_inscripcion = timezone.now()
        id_estudiante=estudiante2.id_estudiante
        inscripcion = Inscripcion(
            fecha_inscripcion=fecha_inscripcion,
            id_curso_id=idcurso,
            id_estudiante_id=id_estudiante,
        )
        inscripcion.save()
        curso=Curso.objects.get(id_curso=idcurso)
        notifacion=Notificacion(
            mensaje=" a "+nombre+" le interesa el curso de "+curso.nombre_curso,
            fecha_creacion=fecha_inscripcion,
            id_inscripcion_id=inscripcion.id_inscripcion,
        )
        notifacion.save()
        
        return render(request, 'Formulario/registro_enviado.html')
    #return redirect('task:formulario_view',idcurso=idcurso)

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def estudiantes_view(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'Estudiante/estudiantes.html', {'estudiantes': estudiantes})   

def logout_view(request):
    logout(request)
    return redirect('task:login')
