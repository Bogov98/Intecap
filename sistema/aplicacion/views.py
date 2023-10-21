from django.shortcuts import render, redirect, get_object_or_404
from .models import CategoriaCurso



def categoriaCursos(request):
    if request.method == 'POST':
        nombre_categoria = request.POST['nombre_categoria']
        descripcion_categoria = request.POST['descripcion_categoria']
        
        # Crea una nueva instancia de CategoriaCurso y guárdala en la base de datos
        nueva_categoria = CategoriaCurso(nombre_categoria=nombre_categoria, descripcion_categoria=descripcion_categoria)
        nueva_categoria.save()
        return redirect('categoria_curso_view')
    
    

def categoria_curso_view(request):
    categorias = CategoriaCurso.objects.all() 
    
    return render(request, 'Categoria/CategoriaCursos.html', {'categorias': categorias})


  
def editar_categoria_view(request,categoria_id):
    categorias = CategoriaCurso.objects.get(id_categoria=categoria_id)
    return render(request, 'categoria/editar_categoria.html',{'categorias':categorias})

def editar_categoria(request, categoria_id):
    if request.method == 'POST':
        categoria=CategoriaCurso.objects.get(id_categoria=categoria_id)
        nombre=request.POST['nombre_categoria']
        descripcion=request.POST['descripcion_categoria']
        categoria=CategoriaCurso(id_categoria=categoria_id, nombre_categoria=nombre, descripcion_categoria=descripcion)
        categoria.save()
        return redirect('categoria_curso_view')
    return render(request, 'Categoria/editar_categoria.html')

def eliminar_categoria(request,categoria_id):
    categoria=CategoriaCurso.objects.get(id_categoria=categoria_id)
    categoria.delete()
    return redirect('categoria_curso_view')
