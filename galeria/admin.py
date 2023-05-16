from django.contrib import admin
from galeria.models import fotografia

# Register your models here.
class listandoFotos(admin.ModelAdmin):
    pass

admin.site.register(fotografia, listandoFotos)