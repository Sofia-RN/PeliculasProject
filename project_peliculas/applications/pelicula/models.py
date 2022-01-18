
from model_utils.models import TimeStampedModel
from django.db import models 

# Create your models here.

class Pelicula(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=120)
    fecha = models.DateField('Fecha', blank=True)
    descripcion = models.CharField('Descripcion', max_length=50)
    rango = models.PositiveIntegerField('Rango', blank=True)
    director = models.CharField('Director', max_length=100)
    autores = models.CharField('Autores', max_length=120)
    duracion = models.CharField('Duracion', max_length=100)
    imagen = models.CharField('Imagen', max_length=100) #modificar luego
    
    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'
    
    def __str__(self):
        return self.nombre
