from django.db import models
from django.utils.text import slugify

# Create your models here.

class EspecialidadesModels(models.Model):
    nombre_especialidad  =  models.CharField(max_length=155)
    descripcion = models.TextField(blank=True, null=True)   
    codigo = models.CharField(max_length=10, unique=True)
    estado = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True,) 

    class Meta:
        verbose_name = "Especialidad Médica"
        verbose_name_plural = "Especialidades Médicas"
        ordering = ['nombre_especialidad']
    
    def save(self, *args, **kwargs):
        # Generar el slug automáticamente basado en el nombre
        if not self.slug:
            self.slug = slugify(self.nombre_especialidad)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre_especialidad


class DoctorModels(models.Model):
    picture =  models.ImageField(upload_to='Imagenes-Medicos')
    nombre_completo =  models.CharField(max_length=255)
    apellido  = models.CharField(max_length=255, null=True)
    tipo_documento = models.CharField(max_length=11, choices=[('DNI','DNI'), ('PASAPORTE', 'Pasaporte'),('CARNET EXT', 'Carnet de Extranjería')], default='DNI')
    numero_documento =  models.IntegerField(null=True)
    Genero = models.CharField(max_length=1, choices=[('M', 'Masculino'),('F', 'Femenino')], default='M')
    especialidad = models.ForeignKey('EspecialidadesModels', on_delete=models.CASCADE, null=True)
    cmp = models.IntegerField()
    experiencia = models.IntegerField()
    ciudad =  models.CharField(max_length=150)
    edad =  models.IntegerField()
    telefono =  models.IntegerField(null=123456789)
    correo_electronico =  models.CharField(max_length=255)
    estado =  models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctores'

