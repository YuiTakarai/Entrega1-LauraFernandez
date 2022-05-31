from django.db import models

# Create your models here.
#para consultar los proveedores:
class Maestro_Proveedores(models.Model):
    vendorID = models.IntegerField()
    vendorname = models.CharField(max_length=40)

#para consultar documentos en la cuenta corriente
class Documentos(models.Model):
    vendorID = models.IntegerField()
    vendorname = models.CharField(max_length=40)
    docnumber = models.CharField(max_length=17)
    docdate = models.DateTimeField()
    docamount = models.FloatField()
    doccurrency = models.CharField(max_length=4)
    centrocosto = models.CharField(max_length=6)
    expensetype = models.CharField(max_length=40)

#para consultar centros de costos.
class CentroCosto(models.Model):
    expensetype = models.CharField(max_length=40)
    centrocosto = models.CharField(max_length=6)

