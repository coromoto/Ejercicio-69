#! /usr/bin/python
#! encoding: UTF-8

#                   nombre,            dirección,                precio promedio,      tipo comida
t_upla_titulos  = ('Nombre: ',        'Dirección: ',             'Precio promedio: ', 'Tipo Comida: ')

def mostrar_restaurante(t, r):
  for i in range(len(t)):
    print t[i], r[i]

# Leer los datos desde un fichero 

# Paso 1: abrir el fichero
fichero = open('10_rest.txt', 'r')

lista_rest = [] 
contador = 0
# Paso 2: leer/escribir los datos en el fichero
while 1:
  n = fichero.readline()
  if n == '':
    break
  nombre = n.rstrip() 
  d = fichero.readline()
  direccion = d.rstrip() 
  p_p = fichero.readline()
  p_p_str = p_p.rstrip() 
  precio_promedio = int(p_p_str) 
  t_c = fichero.readline() 
  tipo_comida = t_c.rstrip() 
  elemento = [nombre, direccion, precio_promedio, tipo_comida]
  lista_rest += [elemento]
  contador += 1

# Paso 3: cerrar el fichero
fichero.close()

for i in lista_rest:
  mostrar_restaurante(t_upla_titulos, i)
