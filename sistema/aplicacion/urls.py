
from django import views
from django.urls import path
from .import views

urlpatterns = [
path('categoria_cursos/', views.categoriaCursos, name='categoria_cursos'),
path('agregar_categoria_curso', views.categoriaCursos, name='agregar_categoria_curso'),

path('mostrar_categorias', views.categoriaCursos, name='mostrar_categorias'),
path('editar_categoria_view/<int:categoria_id>/', views.editar_categoria_view, name='editar_categoria_view'),
path('agregar_categoria_curso', views.editar_categoria, name='agregar_categoria_curso'),
path('editar_categoria/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
path('categoria_cursos_view/', views.categoria_curso_view, name='categoria_curso_view'),
path('eliminar_categoria/<int:categoria_id>/', views.eliminar_categoria, name='eliminar_categoria'),



]


