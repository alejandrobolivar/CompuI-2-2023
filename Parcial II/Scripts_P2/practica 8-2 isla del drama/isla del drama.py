'''Está por terminar la primera temporada del Reality Show llamado “La Isla del
Drama”; razón por la cual se debe iniciar el proceso de selección de los nuevos
participantes para la segunda temporada.
La selección es realizada por tres jueces que emiten una puntuación entre 0.0
y 10.0, por cada candidato que realice la audición.
El problema es que son tantos los candidatos para la audición que la empresa
productora desea que usted realice un programa que procese una lista de
candidatos evaluados que contiene la siguiente información:

NOMBRE DEL CANDIDATO Y LAS 3 PUNTUACIONES DE LOS JUECES.

Dicha información se encuentra almacenada en un archivo de nombre PUNTUACIONES.TXT. Procese la información
y determine e imprima por pantalla.
✓ Porcentaje de candidatos que fueron seleccionados como participantes del reality show.
✓ Promedio de la puntuación definitiva obtenida por los candidatos que pasaron a ser participantes.
✓ Un mensaje que indique si es necesario o no una segunda etapa de selección.
Consideraciones:
✓ La puntuación definitiva de un candidato es el promedio de las 3 puntuaciones emitidas por los jueces.
✓ Un candidato es seleccionado como participante si la puntuación definitiva es mayor o igual a 7.5 puntos.
✓ Se necesita una segunda etapa de selección, si la cantidad de candidatos seleccionados es menor a 20 o
es mayor a 24.'''

arch1 = open('puntuaciones.txt', 'r')

contenido = arch1.readlines()

# inicializacion
linea = 1
cont = 0
suma_def = 0

n = int(contenido[0])

for i in range(n):
    
    lista = contenido[linea].split(',')
    linea += 1
    
    nombre = str(lista[0])
    p1 = int(lista[1])
    p2 = int(lista[2])
    p3 = int(lista[3])
    
    suma = p1 + p2+ p3
    
    defi = suma / 3
    
    if defi > 7.5:
        print(nombre, ' fue seleccionado')
        cont += 1
        suma_def += defi 
    else:
        print(nombre, ' no fue seleccionado')

por = cont / n *100

print('%d' % por, ' % de los candidatos fueron seleccionados')

prom_selec = suma_def / cont

print('el promedio de la puntuación definitiva de los seleccionados es de %.2f' % prom_selec)

if (cont < 20) or (cont > 24):
    print('se necesita una segunta etapa de seleccion')

arch1.close()