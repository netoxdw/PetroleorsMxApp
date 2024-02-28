from django.db import models

# Create your models here.
class Autor(models.Model):
    nombres = models.CharField('Nombres de autor', max_length = 250, null = False, blank = False)
    apellidos = models.CharField('Apellidos de autor', max_length = 250, null = False, blank = False)
    institucion = models.CharField('Escuela/Empresa', max_length= 100, null=True, blank=True)
    nacionalidad = models.CharField('Nacionalidad', max_length=100, null=True, blank=True)
    linkedin = models.URLField('LinkedIn', null = True, blank = True)
    facebook = models.URLField('Facebook', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)
    twitter = models.URLField('x', null = True, blank = True)
    email = models.EmailField('Email', null = False, blank = False)
    estado = models.BooleanField('Activo/Desactivado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nombres