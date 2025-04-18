from django.db import models

# Create your models here.
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def _str_(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()

    def _str_(self):
        return self.titulo