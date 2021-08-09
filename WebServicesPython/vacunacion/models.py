from django.db import models

# Create your models here.
class ciudadanos(models.Model):
    nombre1 = models.CharField(max_length=20)
    nombre2 = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20)
    cedula = models.CharField(max_length=10)
    provincia = models.ForeignKey(provincias, on_delete=models.PROTECT, related_name="ciudadanos")
    canton = models.ForeignKey(cantones, on_delete=models.PROTECT, related_name="ciudadanos")
    parroquia = models.ForeignKey(parroquias, on_delete=models.PROTECT, related_name="ciudadanos")
    centroVacunacion = models.ForeignKey(centro_vacunacion, on_delete=models.PROTECT, related_name="ciudadanos")
    primeraDosis = models.CharField(max_length=30)
    segundaDosis = models.CharField(max_length=30)

class centro_vacunacion(modelos.Model):
    canton = models.ForeignKey(cantones, on_delete=models.PROTECT, related_name="centro_vacunacion")
    centro_vacunacion = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)

class provincias(models.Model):
    canton = models.ForeignKey(cantones, on_delete=models.PROTECT, related_name="centro_vacunacion")

class cantones(models.Model):
    canton = models.ForeignKey(cantones, on_delete=models.PROTECT, related_name="centro_vacunacion")

class parroquias(models.Model):
    canton = models.ForeignKey(cantones, on_delete=models.PROTECT, related_name="centro_vacunacion")