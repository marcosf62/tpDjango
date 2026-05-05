from django.contrib import admin
from .models import Cursos, Prof

admin.site.register(Prof)

@admin.register(Cursos)
class TareaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre","nivel","profe")
    list_filter = ("nombre","profe")
    search_fields = ("nombre",)