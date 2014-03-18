#! /usr/bin/python
#! encoding: UTF-8

#                   nombre,            dirección,                precio promedio,      tipo comida
t_upla_titulos  = ('Nombre: ',        'Dirección: ',             'Precio promedio: ', 'Tipo Comida: ')
rest_sf =         ['Tasca Sin Freno', 'Av. de la Candelaria, 8', 20                 , 'canaria']
rest_ec =         ['El cortijo',      'Bartolome Cairasco, 100', 10                 , 'andaluza']

def mostrar_restaurante(t, r):
  print t[0], r[0]
  print t[1], r[1]
  print t[2], r[2]
  print t[3], r[3]

dic_rest = { 922311231 : rest_sf, 922311232 : rest_ec } 

print(dic_rest)

for i in dic_rest:
  mostrar_restaurante(t_upla_titulos, dic_rest[i])

