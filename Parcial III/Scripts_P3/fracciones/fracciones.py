# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 08:19:29 2022
Solucion del ejercicio de operaciones con fracciones
@author: Prof Alejandro Bolívar
Fecha: 19-04-2022

Operaciones con Fracciones
OBJETIVO: Resolver mediante el uso de subprogramas.
Problema
El departamento de matemáticas pretende corregir un examen en línea de operaciones con fracciones, que se aplicará a un grupo de estudiantes del curso introductorio. Cuando un estudiante realiza la evaluación del tema, se crea
el archivo "examen.txt", en él se almacena la siguiente información: en la primera línea del archivo se encuentra la
identificación del estudiante (Nombre y cédula) y en líneas separadas se guarda, Tipo de operación a realizar (1 = Suma,
2 = Resta, 3 = Multiplicación y 4 = división), las dos fracciones a las que se les va a realizar la operación y la respuesta al
ejercicio dada por el estudiante, en la forma de fracción mixta. Las fracciones que se van a utilizar se generan
aleatoriamente. Además, la evaluación consiste en resolver cinco (5) operaciones, con un puntaje de 4 ptos c/u.
Enunciado
Elabore un programa que dado el archivo "examen.txt", el cual contiene la evaluación realizada por un estudiante,
procese la información con el fin que determine e imprima por pantalla, para cada operación evaluada: la
representación de la operación, la respuesta correcta y un mensaje que indique respondió bien o no el estudiante,
Además, al final se debe mostrar el puntaje total obtenido por el estudiante en el examen presentado, tomando en
cuenta lo indicado anteriormente.

Requerimientos
• Desarrolle un subprograma que reciba dos valores enteros A y B; y retorne el cociente entero y el residuo de la
división de A entre B. Ejemplo, Si A=7 y B=3 => Cociente entero es 2 y el residuo entero es 1.
• Desarrolle un subprograma que reciba una fracción de la forma (a/b) y retorne tres valores (c, r, b) que
representan una fracción mixta de la forma (c a/b), donde:
sí a <= b, c es Cero (0) y r es el valor original de A y
sí a > b, c es el cociente entero de A/B y R es el residuo entero de a/b
• Desarrolle un subprograma que reciba dos fracciones la forma (a/b) y (c/d), retorne la suma de las dos
fracciones, representando la solución en forma de fracción, sabiendo que la fracción resultante es:
num/den = a*d + b*c / (b*d)
• Desarrolle un subprograma que reciba dos fracciones la forma (a/b) y (c/d), retorne la multiplicación de la
primera fracción por la segunda, sabiendo que la fracción resultante es:
num/den = a*c / (b*d)
• Desarrolle un subprograma que reciba dos fracciones la forma (a/b) y (c/d), retorne la división de la primera
fracción entre la segunda, sabiendo que la fracción resultante es:
num/den = a*d / (b*c)
• Desarrolle un subprograma que reciba dos fracciones mixtas y devuelva si las fracciones son iguales o no.
• Un subprograma que imprima una fracción por pantalla de la forma (a/b).

Ejemplo del archivos de entrada y salida por pantalla:
1,  8,  2,  3,  4,  4,  6,  8
4,  3,  9,  6,  4,  1,  2,  9
3,  5,  9,  1,  1,  0,  5,  9
2,  6,  3,  4,  8,  1, 12, 24
4, 10,  5,  4,  3,  1, 10, 20

Pantalla de salida
( 8/ 2) + ( 3/ 4) = 4( 6/ 8) Correcto
( 3/ 9) / ( 6/ 4) = 0(12/54) Incorrecta
( 5/ 9) * ( 1/ 1) = 0( 5/ 9) Correcto
( 6/ 3) – ( 4/ 8) = 1(12/24) Correcto
(10/ 5) / ( 4/ 3) = 1(10/20) Correcto
Puntaje obtenido = 16 ptos.

"""
# subprograma de lectura de los datos de una vuelta
def leer(registro):
    linea = registro.split(',')
    op = int(linea[0])
    num1 = int(linea[1])
    den1 = int(linea[2])
    num2 = int(linea[3])
    den2 = int(linea[4])
    cocr = int(linea[5])
    numr = int(linea[6])
    denr = int(linea[7])
    return op, num1, den1, num2, den2, cocr, numr, denr

# Procedimiento que divide dos numeros y regresa el cociente y residuo de la division
def divisionentera(a, b):
    coc = a // b
    res = a % b
    return coc, res

# Procedimiento que forma una fraccion mixta a partir de una fraccion
def fraccionmixta(a, b):
    if a <= b:  # fracción propia
        c = 0
        r = a
    else:       # fracción impropia
        c, r = divisionentera(a, b)
    return r, c, b

# Procedimiento que suma dos fracciones
def sumafraccion(a, b, c, d):
    num = a * d + b * c
    den = b * d
    return num, den

# Procedimiento que Resta dos fracciones
def restafraccion(a, b, c, d):
    num = a * d - b * c
    den = b * d
    return num, den

# Procedimiento que Multiplica dos fracciones
def multiplicafraccion(a,b,c,d):
    num = a * c
    den = b * d
    return num, den

# Procedimiento que Divide dos fracciones
def dividafraccion(a, b, c, d):
    num = a * d
    den = b * c
    return num, den

# Función que compara dos fracciones mixtas y devuelve si son iguales o no
def iguales(c1, r1, b1, c2, r2, b2):
    return (c1 == c2) and (r1 == r2) and (b1 == b2)

# procedimiento que imprime por pantalla una fraccion
def imprimirfraccion(num, den):
    print(" (%d / %d) " % (num, den), end="")

def main():

    # Que tengo
    num1: int
    den1: int  # Fraccion 1
    num2: int
    den2: int  # Fraccion 2
    op: int
    cocr: int  # Fraccion mixta resultante por el estudiante
    numr: int
    denr: int
    # Que Quiero
    punt: int = 0  # Puntaje obtenido, Acumulador
    # Variables auxiliares
    coc: int
    num: int
    den: int  # Fraccion mixta correcta
    i: int

    arch = open("examen.txt", "r")
    punt = 0
    # Ciclo de lectura
    for registro in arch:
        op, num1, den1, num2, den2, cocr, numr, denr = leer(registro)

        # Determinacion del resultado correcto a la operacion a realizar e
        # Impresion del resultado
        imprimirfraccion(num1, den1)

        if op == 1:
            num, den = sumafraccion(num1, den1, num2, den2)
            print("+", end="")
        elif op == 2:
            num, den = restafraccion(num1, den1, num2, den2)
            print("-", end="")
        elif op == 3:
            num, den = multiplicafraccion(num1, den1, num2, den2)
            print("*", end="")
        else:
            num, den = dividafraccion(num1, den1, num2, den2)
            print("/", end="")

        imprimirfraccion(num2, den2)

        # Determinacion de la fraccion mixta resultante
        num, coc, den = fraccionmixta(num, den)
        print("= %d" % coc, end="")
        imprimirfraccion(num, den)

        if iguales(cocr, numr, denr, coc, num, den):
            print(" Correcto")
            punt += 4
        else:
            print(" Incorrecta")

    # Impresion del puntaje obtenido
    print ("Puntaje Obtenido = %d Ptos" % punt)
    arch.close()

    # Mensaje al usuario
    input("Pulse una tecla para finalizar")

if __name__ == "__main__":
    main()