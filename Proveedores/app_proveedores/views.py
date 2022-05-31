from django.shortcuts import render
from app_proveedores.models import *
from django.http import HttpResponse
import datetime
from django.template import loader
from app_proveedores.forms import *


# Create your views here.

def inicio(request):
    return render (request, "index.html")

def menu(request):
    return render (request, "menu.html")

def altaproveedores(request):
    if request.method == "POST":
        datos_proveedores = AltaProveedores(request.POST)

        if datos_proveedores.is_valid():
            datos = datos_proveedores.cleaned_data
            proveedor = Maestro_Proveedores(vendorID=datos['vendorID'] , vendorname=datos['vendorname'])
            proveedor.save()

            return render( request , "altaproveedores.html")
    return render(request, "altaproveedores.html")

def altadocumentos(request):
    if request.method == "POST":
        altadoc = AltaDocumentos( request.POST )

        if altadoc.is_valid():
            datos_alta = altadoc.cleaned_data
            documento = Documentos(vendorID=datos_alta['vendorID'] , vendorname=datos_alta['vendorname'] , docnumber=datos_alta['docnumber'] , docdate=datos_alta['docdate'] , docamount=datos_alta['docamount'], doccurrency=datos_alta['doccurrency'] , centrocosto=datos_alta['centrocosto'] , expensetype=datos_alta['expensetype'] )
            documento.save()

            return render( request , "altadocumentos.html")
        else: 
            return HttpResponse("el alta no fue satisfactoria")
    return render(request, "altadocumentos.html")

def altacentrocosto(request):
    if request.method =="POST":
        altaceco = AltaCentroCosto(request.POST)
        if altaceco.is_valid():
            datosalta = altaceco.cleaned_data
            alta = CentroCosto (expensetype=datosalta['expensetype'] , centrocosto=datosalta['centrocosto'])
            alta.save()
        return render (request, "altacentrocosto.html")
    return render (request, "altacentrocosto.html")



def consultas(request):
    return render (request , "consultas.html")

def resultadobusqueda(request):
    if request.GET['vendorID']:
        print("este es el error:" , request.GET['vendorID'])
        cuitnro = request.GET['vendorID']
        datos = Maestro_Proveedores.objects.filter(vendorID__icontains = cuitnro)
        return render (request , "resultadobusqueda.html" , {"datos": datos})

def consultas2(request):
    return render (request , "consultas2.html")
    
def resultadobusqueda2(request):
    if request.GET['centrocosto']:
        print("este es el error:" , request.GET['centrocosto'])
        ccnro = request.GET['centrocosto']
        datos_1 = Documentos.objects.filter(centrocosto__icontains = ccnro)
        return render (request , "resultadobusqueda2.html" , {"datos_1": datos_1})

def consultas3(request):
    return render (request , "consultas3.html")
    
def resultadobusqueda3(request):
    if request.GET['centrocosto']:
        print("este es el error:" , request.GET['centrocosto'])
        ccnro2 = request.GET['centrocosto']
        datos_2 = CentroCosto.objects.filter(centrocosto__icontains = ccnro2)
        return render (request , "resultadobusqueda3.html" , {"datos_1": datos_2})


def maestroproveedores(request):
    maestro = Maestro_Proveedores.objects.all()
    proveedores = {"proveedores": maestro}
    return render (request , "maestroproveedores.html" , proveedores)

def documentos(request):
    document = Documentos.objects.all()
    documents = {"documents": document}
    return render (request , "documentos.html" , documents)

def centrodecostos(request):
    ceco = CentroCosto.objects.all()
    ccdatos = {"ccdatos": ceco}
    return render (request , "centrodecostos.html" , ccdatos)


