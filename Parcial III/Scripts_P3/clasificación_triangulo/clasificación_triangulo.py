'''
Escenario: Clasificación de Triangulos
Solución: 1.0 (Estilo modulada)
'''
from math import sqrt

# Subprograma que determina la distancia entre dos puntos
def Distancia(x1:float,  y1:float,  x2:float,  y2:float) -> float:
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Subprograma que verifica si dos numeros son iguales en base a una tolerancia
def Iguales(A:float, B:float, Tol:float) -> bool:
    return abs(A - B) < Tol

# Subprograma que devuelve que tipo de triangulo forma tres vertices: 1(Equilatero), 2(Isoseles) o 3(escaleno
def TipoTriangulo(x1:float, y1:float, x2:float, y2:float, x3:float, y3:float) -> int:
    tt: int
    # La tolerancia es un valor que establecemos.
    Tolerancia:float = 0.001

    # Determinacion de la distancia entre los vertices
    D12: float
    D13: float
    D23: float
    D12 = Distancia(x1, y1, x2, y2)
    D13 = Distancia(x1, y1, x3, y3)
    D23 = Distancia(x2, y2, x3, y3)

    # Clasificacion del triangulo que se forma
    tt = 3
    if Iguales(D12, D13, Tolerancia) and Iguales(D12, D23, Tolerancia):
        tt = 1
    elif Iguales(D12, D13, Tolerancia) or Iguales(D12, D23, Tolerancia) or Iguales(D13, D23, Tolerancia):
        tt = 2

    return tt

# subrpogramas adicionales planteados:
# Subprograma que lee de un archivo las coordenadas de un vertice del triangulo almacenado en el archivo
# Vertices.Txt
def LeerVertice(lista:list, pos:int):
    x= float(lista[pos])
    y= float(lista[pos + 1])
    return x, y

# Subprograma que imprime las coordenadas de un punto en un archivo sin salto de linea
def ImprimirVertice(x:float, y:float):
    arch2.write(f'({x:.2f}, {y:.2f})')

# Subprograma que determina el area de un triangulo emplando el metodo del semiperimetro
def AreaTriangulo(D12:float, D13:float, D23:float) -> float:
    S: float
    S = (D12 + D13 + D23) / 2
    return sqrt(S * (S - D12) * (S - D13) * (S - D23))

# Procedimiento de arranque

# Que tengo
X1: float
Y1: float
X2: float
Y2: float
X3: float
Y3: float # Coordenadas de los vertices de un triangulo

# Que quiero
Tipo: int  # Tipo de triangulo
Area: float   # Area del triangulo

# Variables auxiliares
d12: float
d13: float
d23: float # Longitudes de los lados del triangulo

# Manejo de Archivos de datos
arch1 = open("vertices.txt", 'r')
arch2 = open("Clasificacion.txt", 'w')

# Impresion del titulo de los resultados
arch2.write(" ( Vertice 1 )  ( Vertice 2 )  ( Vertice 3 )  Tipo  Area\n")

# Ciclo de lectura
while True:
    linea = arch1.readline()
    if linea == '':
        break

    lst_vertices = linea.split(',')

    X1, Y1 = LeerVertice(lst_vertices, 0)
    X2, Y2 = LeerVertice(lst_vertices, 2)
    X3, Y3 = LeerVertice(lst_vertices, 4)

    # Determinación de las longitudes de los lados del triangulo
    d12 = Distancia(X1, Y1, X2, Y2)
    d13 = Distancia(X1, Y1, X3, Y3)
    d23 = Distancia(X2, Y2, X3, Y3)

    # Determinacion de los valores pedidos
    Tipo = TipoTriangulo(X1, Y1, X2, Y2, X3, Y3)
    Area = AreaTriangulo(d12, d13, d23)

    # Impresion de los resultados
    ImprimirVertice(X1, Y1)
    ImprimirVertice(X1, Y2)
    ImprimirVertice(X3, Y3)
    arch2.write(f' {Tipo}, {Area:.2f} \n')

# Cierre de archivos
arch1.close()
arch2.close()

# Mensaje al usuario
input("El programa se ha ejecutado en forma exitosa, Pulse una tecla para finalizar")