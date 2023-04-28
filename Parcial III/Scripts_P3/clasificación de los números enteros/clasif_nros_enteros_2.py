# -*- coding: utf-8 -*-
''' Enunciado: Manejo de funciones ejercicio 2 (Clasificacion de numeros)
Elaborado por: Alejandro Bolívar
Fecha: 17-04-2022

Ejercicio 2: Clasificación de los números enteros
Los números enteros se clasifican en ABUNDANTE, DEFICIENTE y PERFECTO,
según la siguiente regla: si la suma de todos los divisores exactos del número
[excluyéndose el número mismo] es mayor, menor o igual al número, respectivamente.
Por ejemplo:
    12 sus divisores son: 1,2,3,4,6 sumados da 16, entonces es abundante
    9 sus divisores son: 1,3 sumados da 4, entonces es deficiente
    6 sus divisores son: 1,2,3 sumados da 6, entonces es perfecto
NOTA: recuerde que al sumar no se toma el mismo número
Enunciado
Desarrolle una aplicación en VB2010 de consola, que lea un grupo de valores enteros,
desde un archivo llamado “numeros.txt” y determine e imprima para cada numero
leído en el archivo “clasificacion.txt”, el número leído y su clasificación
(ABUNDANTE, DEFICIENTE o PERFECTO)
Requerimientos
1. Desarrolle un subprograma que dado un número entero, retorne la sumatoria
de sus divisores exactos.
2. Desarrolle un subprograma que dado un número entero, retorne si éste es
ABUNDANTE, DEFICIENTE o PERFECTO. El valor de salida puede ser del tipo que Ud. quiera.
Ejemplo de los archivos de entrada y salida.

Numero.txt
12
9
6
Clasificacion.Txt
12 Abundante
9 Deficiente
6 Perfecto
'''

def sumatoria(m):
    s = 0
    for i in range(1, m):
        if (m % i == 0):
            s += i
    return s

def tipodenumero(n):
    tipodenumero = "ABUNDANTE"  # Supuesto sumatoria(n) > n
    if sumatoria(n) < n:
        tipodenumero = "DEFICIENTE"
    elif sumatoria(n) == n:
        tipodenumero = "PERFECTO"
    return tipodenumero

arch1 = open("numeros.txt", "r")
arch2 = open("clasificacion.txt", "w")

for registro in arch1:
    t = tipodenumero(int(registro))
    arch2.write(t + "\n")

# Cierre de archivos
arch1.close()
arch2.close()

# Mensaje al usuario
input("Pulse una tecla para finalizar")
