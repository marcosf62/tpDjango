from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('cursos/', views.listaCursos, name='cursoslista'),
    path('', views.bienvenida, name='home'),
]