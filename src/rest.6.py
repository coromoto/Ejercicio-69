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

def archivar_restaurante(f, r):
  f.write( r[0]      + '\n')
  f.write( r[1]      + '\n')
  f.write( str(r[2]) + '\n')
  f.write( r[3]      + '\n')

dic_rest = { 1231 : rest_sf, 1232 : rest_ec } 

print(dic_rest)

for i in dic_rest:
  mostrar_restaurante(t_upla_titulos, dic_rest[i])

# Almacenar los datos de forma permanente

# Paso 1: abrir el fichero
fichero = open('mificheroconrestaurantes.txt', 'w')
# Paso 2: leer/escribir los datos en el fichero
for i in dic_rest:
  #archivar_restaurante(fichero, dic_rest[i])
  fichero.write( dic_rest[i][0]      + '\n')
  fichero.write( dic_rest[i][1]      + '\n')
  fichero.write( str(dic_rest[i][2]) + '\n')
  fichero.write( dic_rest[i][3]      + '\n')

# Paso 3: cerrar el fichero
fichero.close()







