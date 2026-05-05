from django.shortcuts import render
from django.http import HttpResponse
from .models import Cursos


def bienvenida(request):
    return render(request,'cursos/inicio.html')

def listaCursos(request):
    cursos = Cursos.objects.all()  # trae todos los cursos de la BD
    return render(request, 'cursos/listaCursos.html', {'cursos': cursos})