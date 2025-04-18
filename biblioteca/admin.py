from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Libro, Autor

admin.site.register(Libro)
admin.site.register(Autor)