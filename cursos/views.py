from django.shortcuts import render, redirect, get_object_or_404
from .models import Cursos, Prof
from .forms import InfoProf


def bienvenida(request):
    return render(request, 'cursos/inicio.html')


def listaCursos(request):
    cursos = Cursos.objects.all()
    profesores = Prof.objects.all()

    return render(request, 'cursos/listaCursos.html', {
        'cursos': cursos,
        'profesores': profesores
    })


def crear_profesor(request):
    if request.method == "POST":
        form = InfoProf(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cursoslista")  
    else:
        form = InfoProf()

    return render(request, "cursos/crear_profesor.html", {"form": form})


def editar_profesor(request, id):
    profesor = get_object_or_404(Prof, id=id)

    if request.method == "POST":
        form = InfoProf(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect("cursoslista")
    else:
        form = InfoProf(instance=profesor)

    return render(request, "cursos/editar_profesor.html", {"form": form})


def borrar_profesor(request, id):
    profesor = get_object_or_404(Prof, id=id)

    if request.method == "POST":
        profesor.delete()
        return redirect("cursoslista")

    return render(request, "cursos/borrar_profesor.html", {"profesor": profesor})