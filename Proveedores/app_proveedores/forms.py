from django import forms

# Create your forms here.
#para cargar los proveedores:
class AltaProveedores(forms.Form):
    vendorID = forms.IntegerField()
    vendorname = forms.CharField(max_length=40)

#para cargar documentos en la cuenta corriente
class AltaDocumentos(forms.Form):
    vendorID = forms.IntegerField()
    vendorname = forms.CharField(max_length=40)
    docnumber = forms.CharField(max_length=17)
    docdate = forms.DateTimeField()
    docamount = forms.FloatField()
    doccurrency = forms.CharField(max_length=4)
    centrocosto = forms.CharField(max_length=6)
    expensetype = forms.CharField(max_length=40)

#para cargar centros de costos.
class AltaCentroCosto(forms.Form):
    expensetype = forms.CharField(max_length=40)
    centrocosto = forms.CharField(max_length=6)