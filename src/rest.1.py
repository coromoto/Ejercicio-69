#! /usr/bin/python
#! encoding: UTF-8

def mostrar_restaurante(n, d, pp, tc):
  print 'Nombre:', n
  print 'Dirección:', d
  print 'Precio Promedio:', pp
  print 'Tipo de Comida:', tc

nombre_1          =  'Tasca Sin Freno'
direccion_1       = 'Av. de la Candelaria, 8'
precio_promedio_1 = 20.0
tipo_comida_1     = 'canaria'

nombre_2          =  'El cortijo'
direccion_2       = 'Bartolome Cairasco, 100'
precio_promedio_2 = 10.0
tipo_comida_2     = 'andaluza'


mostrar_restaurante(nombre_1, direccion_1, precio_promedio_1, tipo_comida_1)
mostrar_restaurante(nombre_2, direccion_2, precio_promedio_2, tipo_comida_2)
