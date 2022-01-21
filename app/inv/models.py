from tabnanny import verbose
from django.db import models

from app.base.models import ClaseModelo

# Create your models here.
class Categoria(ClaseModelo):
    descripcion = models.CharField('Descripción de la Categoría', max_length=100,unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save() 
    
    class Meta:
        verbose_name_plural = "Categorias"
        ordering = ['descripcion']

        
