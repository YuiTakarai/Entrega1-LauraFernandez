from django.shortcuts import render
from app_proveedores.models import *
from django.http import HttpResponse
import datetime
from django.template import loader
from app_proveedores.forms import *


# Create your views here.

def inicio(request):
    return render (request, "index.html")
