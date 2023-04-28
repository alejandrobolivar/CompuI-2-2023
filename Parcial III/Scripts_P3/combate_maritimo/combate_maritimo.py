'''
ESCENARIO: SIMULACIÓN DE COMBATE MARITIMO
El Ministerio de defensa del país, en el presente mes a recibido unos buques de
guerras los cuales dispones de una batería de cañones los cuales quieren adaptar a
los sistemas de control existentes. Estos conociendo su gran conocimiento en
programación lo contratan para que diseñe un programa de simulación de las
características del lanzamiento de las bombas de un cañón a sus diferentes blancos
enemigos. Las características del disparo del cañón a utilizar por el programa son:
ángulo de disparo y la información de cada uno de los blancos a acertar, toda esta
información almacenada en el archivo “Simulacro.txt” y se desea determinar la
velocidad del disparo para dar en el blanco de ser posible. Para cada disparo a
efectuar se tiene la siguiente información:
Tipo de blanco (0= Marítimo y 1 = aéreo), distancia horizontal de alcance y altura del blanco.
NOTA: Se conoce que por el diseño de los cañones su ángulo de inclinación solo se puede adaptar una sola vez en el combate.
Además, la velocidad de salida de la bala se encuentra entre 35 a 85m/s.

PROBLEMA
Elabore una aplicación en VB2010 bajo consola, que dada la información del ángulo del disparo y un grupo de blancos a atacar,
almacenado en el archivo de datos “Simulacro.txt” determine e imprima por pantalla para cada blanco:
Tipo de blanco, Velocidad de salida(m/s) y Situación del disparo.
Donde la Situación del disparo de ser posible: 0 = Muy cerca (vel<35m/s), 1 = acierta en el blanco(35m/s ≤ vel ≤ 85m/s) o 2 = Muy lejos (vel>85m/s).
Sino es posible el disparo emitir un mensaje que indique, “ángulo no apropiado”
Además para todos los blancos: porcentaje de blancos que están fuera del alcance del cañón, por culpa del ángulo del disparo.

REQUERIMIENTOS
Construya e implemente los siguientes Subprogramas:
1- Un subprograma que dado un ángulo en grados determine su valor en radianes.
2- Un subprograma que dada la distancia horizontal(x), altura del blanco (y) y ángulo(α) de salida del disparo devuelva,
si es positivo el valor de (x*tan(α)-y) o no.
3- Un subprograma que dada la distancia horizontal(x), altura del blanco (y) y el ángulo(α)
de salida del disparo devuelva, la velocidad de salida del disparo y situación del disparo
(Según como se especifica en enunciado). Donde:
Velocidad = Math.Sqrt(g / (2 * (X * Math.Tan(Alfa) - Y))) * (X / Math.Cos(Alfa))
Observación: Para el caso de ser el enemigo un blanco aéreo, dependiendo de la altitud y distancia que tenga el blanco, el
disparo llegue a ser imposible

Recuerde
1 π (radianes) = 180º
g=9.81m/s2
Las funciones requeridas de VB2010, tienen la siguiente manera de llamado:
Math.cos(Angulo_radianes) ‘coseno del ángulo en radianes
Math.tan(Angulo_radianes) ’Tangente del ángulo en radianes
Math. sqrt(valor_x) ‘Raíz cuadrada de x

Ejemplo de Cálculo
Ángulo del disparo: 49,8 ° = 0,869 rad
Nro Blancos: 4
Tipo de blanco Alcance(x) Altura(y) x*tan(α)-y Vel Situación
1 219,41 403,03 -143,48 Angulo no apropiado
0 492,61 1,1 581,62 70,07 1
1 397,92 324,93 145,78 113,02 2
0 26 -1,11 31,87 15,80 0
Porcentaje de disparos fuera del ángulo: 25,00%
'''
import math
# Requerimientos
# 1.-
def Grados_a_Radianes(Grado: float):
    # 360° = 2 Pi radianes => 180° = Pi Radianes => X° = (X*Pi)/180 radianes
    return (Grado * math.pi) / 180


# 2.-
def Verificar(X: float, Y: float, Alfa: float):
    return X * math.tan(Alfa) - Y > 0


# 3.-
def Calculos(X: float, Y: float, Alfa: float):
    G = 9.81 # m/s^2

    Velocidad = math.sqrt(G / (2 * (X * math.tan(Alfa) - Y))) * (X / math.cos(Alfa))

    if Velocidad < 35:
        Situacion = 0
    elif Velocidad <= 85:
        Situacion = 1
    else:
        Situacion = 2

    return Velocidad, Situacion


def main():
    # Variables a leer del Archivo
    Angulo_del_Disparo: float # Grados
    Tipo_de_Blanco: int # 0=Marítimo, 1=Aéreo
    Distancia_Horizontal: float
    Altura_del_Blanco: float
    # Variables a mostrar al Usuario
    Velocidad_de_Salida: float # m/s
    Situacion_del_Disparo: int # 0=Muy cerca, 1=Acierta el blanco, 2=Muy Lejos
    Por: float # % de blancos que estan fuera del alcance del cañon
    # Variables de proceso
    Angulo: float # Angulo de disparo en Radianes
    C1: int # cantidad de blancos que estan fuera del alcance del cañon
    CT: int # cantidad total de blancos

    # Apertura y Modo de uso del Archivo
    arch = open("simulacro.txt", 'r')
    contenido = arch.readlines()
    linea = 1  # Posición del siguiente elemento

    # Iniciación de variables
    C1 = 0
    CT = 0
    # Proceso
    Angulo_del_Disparo = float(contenido[0])
    Angulo = Grados_a_Radianes(Angulo_del_Disparo)
    print("Angulo= %.2f" % Angulo_del_Disparo)
    for i in range(len(contenido)-1):

        listaint = contenido[linea].split(',')
        Tipo_de_Blanco = int(listaint[0])
        Distancia_Horizontal = float(listaint[1])
        Altura_del_Blanco = float(listaint[2])

        linea +=1

        CT = CT + 1
        if Verificar(Distancia_Horizontal, Altura_del_Blanco, Angulo):
            Velocidad_de_Salida, Situacion_del_Disparo = Calculos(Distancia_Horizontal, Altura_del_Blanco, Angulo)
            print("Tipo de Blanco= %d Velocidad de Salida= %.2f Situacion= %d" % (Tipo_de_Blanco, Velocidad_de_Salida, Situacion_del_Disparo))
        else:
            C1 = C1 + 1
            print("Tipo de Blanco= %d Angulo no apropiado" % Tipo_de_Blanco)


    # Calculo e impresión de resultados totales
    Por = C1 / CT * 100
    print("Porcentaje de Blancos fuera de alcance= %.2f %%" % Por)

    # Mensaje al usuario
    input("Pulse una tecla para finalizar")

if __name__ == "__main__":
    main()