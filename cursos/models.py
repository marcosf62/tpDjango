from django.db import models

class Cursos (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel = models.CharField(max_length=50)  # Ej: Básico, Intermedio, Avanzado
    duracion_semanas = models.IntegerField()

    def __str__(self):
        return self.nombre