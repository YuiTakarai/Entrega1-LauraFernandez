# Entrega1-LauraFernandez
Proyecto Gestion de Proveedores Web.
Este proyecto es parte de las entregas programadas para el curso de Python en CoderHouse.
Se trata de una web creada con Djagno y Python, utilizando como css: "startbootstrap-one-page-wonder".

El proyecto simula una web de gestión de proveedores, el mismo sigue en desarrollo. 
Para que la web sea funcional falta desarrollar:
  Login para diferentes niveles de usuarios.
  Campos adicionales para ingresar información de los documentos legales (CAE, Impuestos, etc.). 
  Módulo tesorería para ingresar ordenes de pago.
  Módulo Orden de Compra.
  Módulo Factura de Crédito PyME. 
  Vinculación con ERP y base de datos externas.
  Vinculación con AFIP para validar CAE.
  Flujo de aprobaciones / rechazos.
  Consulta de cuenta corriente.
  Exportación a Excel y otros.

Como navegar la versión vigente:
a) Desde index.html se puede acceder al menú. 
b) Desde menu.html se puede acceder a tres formularios para cargar información: altaproveedores.html; altacentrocosto.html & altadocumento.html.
c) en altaproveedores.html se solicita dos datos, CUIT (campo numérico) y RAZON SOCIAL (campo texto). Estos datos se guardan en la base de datos MaestroProveedores.
d) en altacentrocosto.html se solicita dos datos, CENTRO DE COSTOS (campo texto) Y TIPO DE GASTO (campo texto). Estos datos se guardan en la base de datos CentroCosto.
e) en altadocumento.html se solicita completar ocho campos CUIT (campo numérico), Razon Social (campo texto), Nro Documento (campo texto), Fecha Documento (campo fecha), Monto Neto (campo numérico), Moneda (campo texto), centro de costo (campo texto) y tipo de gasto (campo texto).
Cada uno de estos campos se almacenan en la base de datos Documentos.
f) en maestroproveedores.html se puede consultar la base de datos completa de proveedores.
g) en centrodecostos.html se puede consultar la base de datos completa de centros de costos.
h) en documentos.html se puede consultar la base completa de documentos registrados.
Por último, existen tres consultas vigentes:
1) Consulta de Proveedores existentes por CUIT. En caso de que el proveedor no exista, devuelve la leyenda "el proveedor no existe"
2) Consulta de Gastos por Centros de Costos. Al ingresar el Centro de Costos genera una tabla con información sobre documentos ingresados a dicho CC.
3) Consulta de Centros de Costos existentes. En caso de que el Centro de Costos no exista, devuelve la leyenda "el centro de costos no existe"


