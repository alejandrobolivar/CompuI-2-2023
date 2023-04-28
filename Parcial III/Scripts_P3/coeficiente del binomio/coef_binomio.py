# -*- coding: utf-8 -*-
'''
Enunciado: Manejo de funciones, Ejercicio 1 (Coeficiente del binomio)
Elaborado por: Alejandro Bolívar
Fecha: 17-04-2022

El triángulo de Pascal es un triángulo de números enteros, infinito y simétrico
cuyas diez primeras líneas han sido representadas en la figura. El cual se
construye de la siguiente manera: Se empieza por el « 1 » de la cumbre.
De una línea a la siguiente se conviene escribir los números con un desfase de
media casilla. Así, las casillas (que no se dibujan) tendrán cada una dos
casillas justo encima, en la línea anterior. El valor que se escribe en una
casilla es la suma de los valores de las dos casillas encima de ella.
el interés de este triángulo no radica en estas propiedades, sino en el vínculo
que tiene con la álgebra elemental. En efecto, las cifras de la tercera fila
(1; 2; 1) y la cuarta fila (1; 3; 3; 1) recuerdan las identidades:
(a+b)2=a2+2ab+b2 y (a+b)3=a3+3a2b+3ab2+b3
pues son los coeficientes de sus monomios. Sin embargo, cuando el exponente es
muy grande calcular los coeficiente de los monomios es muy tedioso, si se
determine empleando el triangulo de Pascal, de esta forma cada coeficiente se
calcula determinando el coeficiente del Binomio, el cual se calcula como la
combinatoria de k en n, donde: k es el coeficiente a determinar y n es el
exponente del binomio. C=n!/(k!(n-k)!)

Enunciado
Desarrolle un programa que lea un grupo de pares de valores enteros, desde un
archivo llamado “datos.txt” y determine para cada par, el coeficiente del
binomio. El resultado debe imprimirse a un archivo llamado “resultados.txt”.
Requerimientos
1. Desarrolle un Subprograma que dado un valor entero N, determine el factorial
de dicho número.
2. Desarrolle un subprograma que dados dos valores enteros k y n, calcule el
coeficiente del binomio, según la fórmula mostrada anteriormente.

Ejemplo de los archivos de entrada y salida.
datos.txt
4, 7
2, 3
5, 9

resultados.txt
Coeficiente 4 para binomio de 7 es: 35
Coeficiente 2 para binomio de 3 es: 3
Coeficiente 5 para binomio de 9 es: 126
'''

# Subprogramas solicitados:
# Subprograma que dado un valor entero N, determine el factorial de dicho número
def factorial(n):
    f = 1
    for i in range (2, n+1):
        f *= i
    return f

# Subprograma que dados dos valores enteros k y n, calcule el coeficiente del binomio, según la formula mostrada anteriormente
def coeficientedelbinomio(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

#  Subprogramas adicionales para modular aún mas el programa
#  Subprograma de lectura del coeficiente del binomio a determinar del archivo de datos
def leer(registro):
    linea = registro.split(',')
    k = int(linea[0])
    n = int(linea[1])
    return k, n

#  Subprograma de impresión de la solución hacia el archivo de salida
def imprimir(arch, n, k, c):
    arch.write(f"coeficiente {str(k)} para binomio de {str(n)} es: {str(c)}" + "\n")

def main():
    # ¿Qué tengo?, Variables de entrada
    n: int  # n es el exponente del binomio.
    k: int  # k es el coeficiente a determinar

    # ¿Qué quiero?, Variables de salida
    c: int  # c es el coeficiente del binomio

    #  Procedimiento de arranque
    #  Manejo de archivos
    arch1 = open("datos.txt", "r")
    arch2 = open("resultados.txt", "w")
    #  Ciclo De lectura
    for registro in arch1:
        k, n = leer(registro)
        #  Proceso a desarrollar
        c = coeficientedelbinomio(n, k)
        imprimir(arch2, n, k, c)

    # Cierre de archivos
    arch1.close()
    arch2.close()

    # Mensaje al usuario
    input("Pulse una tecla para finalizar")

if __name__ == "__main__":
    main()