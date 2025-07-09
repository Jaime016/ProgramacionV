#from django.db import models

# Create your models here.

from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    puntaje = models.DecimalField(max_digits=3, decimal_places=2)  # ejemplo: 4.75
    comentario = models.TextField(blank=True)

    def __str__(self):
        return f"{self.puntaje} - {self.comentario[:20]}"

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    calificacion = models.ForeignKey(Calificacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
