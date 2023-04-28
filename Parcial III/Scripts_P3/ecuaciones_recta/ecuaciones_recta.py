# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:32:04 2022

@author: bolivar

' Respuesta del ejercicio de las ecuaciones de la recta
' Elaborado por: Prof. Alejandro Bolívar
' Fecha: 20-04-2022

La ecuación general de una recta en el plano cartesiano puede expresarse
según su ecuación general:
a * Y + b * X + c = 0
tal representación permite incluir las distintas ubicaciones relativas de una
recta con los ejes X, Y del plano cartesiano, de acuerdo con la siguiente
clasificación:
Tipo 1: Horizontales. Por ejemplo,
Parámetros de la recta
Punto de intersección con el eje Y: i_ejeY(0,3) = (0, -c/a)
Tipo 2: Verticales. Por ejemplo,
Parámetros de la recta
Punto de intersección con el eje X: i_ejeX(-2, 0)
Tipo 3: Oblicuas. Por ejemplo,
Parámetros de la recta
Punto de intersección con el eje X: i_ejeX(-1, 0)
Punto de intersección con el eje Y: i_ejeY( 0,1)

Dado un archivo de datos "datos.txt" que almacena en cada línea dos puntos que
conforman un segmento de recta, desarrolle un programa que emplee subprogramas
donde: determine e imprima en el archivo "resultados.txt", para cada segmento
de recta que conforman los dos puntos, su posición relativa en el plano cartesiano:
    Tipo 1, 2, ó 3, los coeficientes (a,b,c) de la ecuación de la recta y los
    puntos de intersección con el "eje x" y con el "eje y" según sea el caso.

Para la solución del problema debe definir y utilizar:
1.	Un subprograma que lea desde archivo de datos las coordenadas (xi, yi) y
(x2, y2) de dos puntos que conforman UNA RECTA.
2.	Un subprograma que calcula a partir de los parámetros de una recta (a, b, c),
la intersección de la recta con el eje x (iX).
3.	Un subprograma que calcula a partir de los parámetros de una recta (a, b, c),
la intersección de la recta con el eje y (iY).
4.	Un subprograma que determine la posición relativa de una recta en el plano
cartesiano (1, 2, ó 3).
5.	Un subprograma que imprima hacía un archivo de resultados a partir de los
parámetros de la recta (a,b,c) y los ínterceptos (ix) (iy) los puntos de
    intersección con los ejes, según sea su posición relativa. Nota: si la
    recta es horizontal (ix = 0) o si la recta es vertical (iy = 0).

Se dispone de un subprograma que dados dos puntos P
los contiene, el cual se muestra a continuación:

Sub ecRecta(ByVal XI As Single, ByVal Y1 As Single, ByVal X2 As Punto, _
ByVal Y2 As Single, ByRef a As Single, ByRef b As Single, Byref c As Single)
    if X1=X2 then
        a=0 : b=1 : c=—XI
    elseif Y1=Y2 then
        a=1 : b=0 : c=—Y1
    else
        a=1 : b=(Y2-Y1)/(X1-X2) : c—(Y1+b*X1)
    end if
End Sub

Ejemplo de los archivos:
datos.txt
-1.0 0.0 0.0 1.0
1.0 3.0 3.0 3.0
-2.0 0.0 -2.0 7.0

respuesta.txt
Recta tipo 3:
(a= 1.0, b=-1.0, c=-1.0); i_ejeX(-1.0, 0.0); i_ejeY(0.0,1.0)
Recta tipo 1:
(a= 1.0, b= 0.0, c=-3.0); i_ejeY( 0.0, 3.0)
Recta tipo 2:
(a= 0.0, b= 1.0, c= 2.0); i_ejeX(-2.0, 0.0)
"""

# SP dado en el enunciado
def ecrecta(x1, y1, x2, y2):
    if x1 == x2:
        a = 0
        b = 1
        c = -x1
    elif y1 == y2:
        a = 1
        b = 0
        c = -y1
    else:
        a = 1
        b = (y2 - y1) / (x1 - x2)
        c = -(y1 + b * x1)
    return a, b, c

# SP que lee dos puntos
def leerpuntos(registro):
    linea = registro.split(',')
    x1 = float(linea[0])
    y1 = float(linea[1])
    x2 = float(linea[2])
    y2 = float(linea[3])
    return x1, y1, x2, y2

# SP que determine el intercepto con el eje X de una recta
def ejex(b, c):
    return -c / b

# SP que determine el intercepto con el eje X de una recta
def ejey(a, c):
    return -c / a

# SP que determine el tipo de recta que representa.
def tipo(a, b):
    tipo = 3  # Supuesto tipo = 3
    if a == 0:
        tipo = 2
    elif b == 0:
        tipo = 1
    return tipo

def imprimir(arch, a, b, c, ix, iy):
    arch.write("Recta tipo: %d\n" % tipo(a, b))
    arch.write("( %.2f, %.2f, %.2f);" % (a, b, c))
    if b == 0:
        arch.write("i_EjeY( 0.00, %.2f)" % iy)
    elif a == 0:
        arch.write("i_EjeX( %.2f, 0.00)" % ix)
    else:
        arch.write("i_EjeX( %.2f, 0.00); " % ix)
        arch.write("i_EjeY( 0.00, %.2f )" % iy)
    arch.write("\n")

def main():

    # Que tengo?
    x1: float
    y1: float
    x2: float
    y2: float

    # Que quiero?
    a: float
    b: float
    c: float
    ix: float
    iy: float
    tr: int

    # Manejo de ciclos
    arch1 = open("datos.txt", "r")
    arch2 = open("respuestas.txt", "w")

    # Ciclo de lectura
    for registro in arch1:
        x1, y1, x2, y2 = leerpuntos(registro)

        # Determinación de los parámetros de la recta
        a, b, c = ecrecta(x1, y1, x2, y2)

        # Determinación del tipo de recta
        tr = tipo(a, b)

        # Determinación de los interceptos con los ejes
        if tr == 1:
            iy = ejey(a, c)
            ix = 0
        elif tr == 2:
            ix = ejex(b, c)
            iy = 0
        else:
            ix = ejex(b, c)
            iy = ejey(a, c)

        # impresión del resultado
        imprimir(arch2, a, b, c, ix, iy)

    # Cierre de archivos
    arch1.close()
    arch2.close()

    # Mensaje al usuario
    print("La ejecución ha finalizado con éxito")

    # Mensaje al usuario
    input("Pulse una tecla para finalizar")

if __name__ == "__main__":
    main()