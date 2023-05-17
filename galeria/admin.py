from django.contrib import admin
from galeria.models import fotografia

# Register your models here.
class listandoFotos(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda")
    list_display_links = ("id", "nome")
    search_field = ("nome",)
    list_filter = ("categoria",)

admin.site.register(fotografia, listandoFotos)