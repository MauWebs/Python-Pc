from django.db import models

class PC(models.Model):
    sistema_operativo = models.CharField(max_length=255)
    version_sistema = models.CharField(max_length=255)
    arquitectura_sistema = models.CharField(max_length=255)
    nombre_usuario = models.CharField(max_length=255)
    nombre_host = models.CharField(max_length=255)
    direccion_ip = models.GenericIPAddressField()
    info_cpu = models.CharField(max_length=255)
    num_cores_fisicos = models.IntegerField()
    num_cores_logicos = models.IntegerField()
    memoria_total = models.FloatField()
    memoria_disponible = models.FloatField()