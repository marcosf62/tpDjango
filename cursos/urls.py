from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('cursos/', views.listaCursos, name='cursoslista'),
    path('profe/', views.crear_profesor, name='profes'),

    path('profesor/editar/<int:id>/', views.editar_profesor, name='editar_profesor'),
    path('profesor/borrar/<int:id>/', views.borrar_profesor, name='borrar_profesor'),
]