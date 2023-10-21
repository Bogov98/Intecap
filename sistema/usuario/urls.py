from django import views
from .import views
from django.urls import path
#from task.views import login_view, register

app_name = 'task'

urlpatterns = [
    path('', views.login_view, name='login'),
    #path('register/', register, name='register'),  
   # path('inicio', views.inicio, name='index'),
    # Otras rutas y configuraciones de URL
<<<<<<< HEAD

=======
<<<<<<< HEAD
    path('inicio', views.inicio, name='inicio'),
=======
<<<<<<< Updated upstream
>>>>>>> 169983e25eaefb433cfe208c447b05903f0ae5b6
    path('inicio', views.inicio, name='inicio'),

    path('inicio/', views.inicio, name='inicio'),
    path('create_curso_view/', views.create_curso_view, name='create_curso_view'),
    path('create_curso/', views.create_curso, name='create_curso'),
    path('curso_view/', views.curso_view, name='curso_view'),
    path('editar_curso_view/<int:idcurso>/', views.editar_curso_view, name='editar_curso_view'),
    path('editar_curso/<int:idcurso>/', views.editar_curso, name='editar_curso'),
    path('eliminar_curso/<int:idcurso>/', views.eliminar_curso, name='eliminar_curso'),
<<<<<<< HEAD

=======
>>>>>>> Stashed changes
>>>>>>> 0c313e38a126b477fc2274d9f2cf9d79774785bf
>>>>>>> 169983e25eaefb433cfe208c447b05903f0ae5b6
    # Otras rutas y configuraciones de URL
]