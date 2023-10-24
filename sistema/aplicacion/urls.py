from django import views
from .import views
from django.urls import path

app_name = 'task'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('', views.login_view, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('create_curso_view/', views.create_curso_view, name='create_curso_view'),
    path('create_curso/', views.create_curso, name='create_curso'),
    path('curso_view/', views.curso_view, name='curso_view'),
    path('editar_curso_view/<int:idcurso>/', views.editar_curso_view, name='editar_curso_view'),
    path('editar_curso/<int:idcurso>/', views.editar_curso, name='editar_curso'),
    path('eliminar_curso/<int:idcurso>/', views.eliminar_curso, name='eliminar_curso'),
    path('search_categoria/', views.search_categoria, name='search_categoria'),
    path('formulario_view/<int:idcurso>/', views.formulario_view, name='formulario_view'),
    path('enviar_formulario/<int:idcurso>/', views.enviar_formulario, name='enviar_formulario'),
    path('estudiantes_view/', views.estudiantes_view, name='estudiantes_view'),
    path('logout/', views.logout_view, name='logout'),
    path('search_curso/', views.search_Curso, name='search_curso'),
    path('estudiante_view/', views.estudiantes_view, name='estudiante_view'),
    path('estudiantes_curso_filtro/<int:idcurso>/', views.estudiantes_curso_filtro, name='estudiantes_curso_filtro'),
    path('editar_estudiante_view/<int:idestudiante>/', views.editar_estudiante_view, name='editar_estudiante_view'),
    path('editar_estudiante/<int:idestudiante>/<int:idcurso>/', views.editar_estudiante, name='editar_estudiante'),
    path('usuarios_view/', views.usuarios_view, name='usuarios_view'),

    
]