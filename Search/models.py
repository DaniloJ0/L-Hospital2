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
    Latitude= models.CharField(max_length=50)
    Longitude= models.CharField(max_length=50)
    
    # class META():
    #     ordering=['Nombre']
        
    # def __str__(self):
    #     return self.Nombre
