# Entrega1-LauraFernandez
Proyecto Gestion de Proveedores Web.
Este proyecto es parte de las entregas programadas para el curso de Python en CoderHouse.
Se trata de una web creada con djagno y python, utilizando como template "startbootstrap-one-page-wonder".
El proyecto simula una web de gestión de proveedores, el mismo sigue en desarrollo. 
Para que la web sea funcional falta desarrollar:
  Login para diferentes niveles de usuarios.
  Más campos para ingresar información de los documentos legales (CAE, Impuestos, etc.). 
  Módulo tesorería para ingresar ordenes de pago.
  Módulo Orden de Compra.
  Módulo Factura de Crédito PyME. 
  Vinculación con ERP y base de datos externas.
  Vinculación con AFIP para validar CAE.
  Flujo de aprobaciones / rechazos.
  Consulta de cuenta corriente.
  Exportación a Excel y otros.

Como navegar la versión vigente:
Desde index.html se puede acceder al menú.
Desde menu.html se puede acceder a la carga de proveedores, centros de costos y documentos. 
Cada vista de carga de información vuelca la misma en la BD correspondiente, de forma tal que luego puede ser vista en los enlaces 
Maestro de Proveedores, Centro de Costos y documentos.
Por último, existen tres consultas vigentes:
a) Consulta de Proveedores existentes por CUIT. En caso de que el proveedor no exista, devuelve la leyenda "el proveedor no existe"
b) Consulta de Gastos por Centros de Costos. Al ingresar el Centro de Costos genera una tabla con información sobre documentos ingresados a dicho CC.
c) Consulta de Centros de Costos existentes. En caso de que el Centro de Costos no exista, devuelve la leyenda "el centro de costos no existe"


Información sobre derechos de autor y licencias.
