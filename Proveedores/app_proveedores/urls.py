from django.urls import path
from app_proveedores.views import *
from app_proveedores import views

urlpatterns = [
    path('' , views.inicio, name = "index"),
    path('menu' , views.menu , name ="menu"),
    path('altaproveedores' , views.altaproveedores , name = "altaproveedores"),
    path('altacentrocosto' , views.altacentrocosto , name ="altacentrocosto"),
    path('altadocumentos' , views.altadocumentos , name = "altadocumentos"),
    path('maestroproveedores' , views.maestroproveedores , name = 'maestroproveedores'),
    path('centrodecostos' , views.centrodecostos , name = "centrodecostos"),   
    path('documentos' , views.documentos , name = 'documentos'),
    path('consultas' , views.consultas , name = "consultas"),
    path('resultadobusqueda', views.resultadobusqueda , name = "resultadobusqueda"),
    path('consultas2' , views.consultas2 , name = "consultas2"),
    path('resultadobusqueda2', views.resultadobusqueda2 , name = "resultadobusqueda2"),
    path('consultas3' , views.consultas3 , name = "consultas3"),
    path('resultadobusqueda3', views.resultadobusqueda3 , name = "resultadobusqueda3")
    ]
    