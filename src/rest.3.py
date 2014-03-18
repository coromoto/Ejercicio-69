#! /usr/bin/python
#! encoding: UTF-8

def mostrar_restaurante(r):
  print 'Nombre:',          r[0]
  print 'Dirección:',       r[1]
  print 'Precio Promedio:', r[2]
  print 'Tipo de Comida:',  r[3]

#           nombre,           dirección,                 precio promedio,  tipo comida
rest_sf = ['Tasca Sin Freno', 'Av. de la Candelaria, 8', 20              , 'canaria']
rest_ec = ['El cortijo',      'Bartolome Cairasco, 100', 10              , 'andaluza']

list_rest = [rest_sf, rest_ec]

for elemento_de_lista in list_rest:
  mostrar_restaurante(elemento_de_lista)
