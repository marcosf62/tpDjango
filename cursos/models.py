from django.db import models

class Prof (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre

class Cursos (models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel = models.CharField(max_length=50)  # Ej: Básico, Intermedio, Avanzado
    duracion_semanas = models.IntegerField()
    profe = models.ForeignKey(Prof, on_delete=models.CASCADE, null=True, default=None, related_name="curso")

    def __str__(self):
        return self.nombre