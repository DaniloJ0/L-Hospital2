from django.db import models

# Create your models here.
class servicio(models.Model):
    ID = models.CharField(max_length=250, primary_key = True)
    Municipio = models.CharField(max_length = 100)
    Nombre = models.CharField(max_length = 100)
    Direccion = models.CharField(max_length = 1000)
    Correo = models.CharField(max_length = 100)
    tipo = models.CharField(max_length = 100)
    Metodologia = models.CharField(max_length = 100)
    Especialidad = models.CharField(max_length = 100)
    ambulatorio	= models.CharField(max_length = 10)
    hospitalario = models.CharField(max_length = 10)	
    unidad_movil = models.CharField(max_length = 10)	
    domiciliario = models.CharField(max_length = 10)
    horario_lunes = models.CharField(max_length = 60)
    horario_martes = models.CharField(max_length = 60)
    horario_miercoles = models.CharField(max_length = 60)	
    horario_jueves = models.CharField(max_length = 60)
    horario_viernes = models.CharField(max_length = 60)
    horario_sabado = models.CharField(max_length = 60)	
    horario_domingo = models.CharField(max_length = 60)
