'''
Ejercicio de tiro al blanco
Elaborado por: Prof. Alejandro Bolívar
Fecha: 30-04-2022

E S C E N A R I O : C O M P E T E N C I A D E T I R O
En una competencia de tiro al blanco abierta al público, se almaceno en el archivo de datos principiantes.txt, la información de
un grupo de participantes, donde en cada línea del mismo se registro: nombre del competidos, categoría a la que pertenece (1=
Juvenil y 2= Mayores), y las coordenadas (X, Y) de los tres disparos realizados hacia la diana, que dependiendo de la categoría al
que pertenece el competidor tiene radios distintos. La competición se clasifico en dos categorías, Juvenil y Mayores. La diana
para la categoría juvenil tiene las siguientes dimensiones de la circunferencia interna a la externa: 2, 4, 6, mientras la categoría
mayores es de 1, 2 y 3. Las puntuaciones del disparo se establece según la zona en que acierte el disparo y esta se muestra en la
imagen adjunta.

ENUNCIADO
Elabore una aplicación en VB2010, que dado el archivo principiantes.txt, determine e
imprima en el archivo correspondiente a su categoría (juvenil.txt o mayores.txt):
    
Para cada Competidor:
• Nombre del competidor y puntuación obtenida.(acumulado de los tres disparos)
Para todos los competidores:
• Porcentaje de competidores que dieron en el centro de la diana
• Promedio de puntos obtenidos.

Requerimientos mínimos del programa:
    
Elabore los siguientes Subprogramas:
1- Un subprograma que lea una línea de un archivo de datos, la cual contiene un
nombre, un valor entero y la coordenada de tres puntos.
2- Un subprograma que dado el radio de una circunferencia (Con centro en el origen) y las coordenadas de un punto
determine, si el punto esta dentro o fuera del circulo formado por la circunferencia.
3- Un subprograma que dadas los radios de tres circunferencias concéntricas en el origen y la coordenada de un disparo,
indique que puntaje este obtiene según los criterios establecidos por la competición.
4- Un subprograma que imprima en un archivo de datos, pasando el nro. del mismo, el nombre de un participante y el
puntaje obtenido en la realización de sus tres disparos.

Ejemplo del archivo de datos:
    
participantes.txt

Jesus M , 1, 1.0, 0.5, 2.0, -8.0, -1.0, 0.5
Marcos P , 2, 0.0, -1.5, 0.0, 0.0, -9.5, 3.5
Luis O , 1, 4.0, -2.0, -1.0, 0.5, 7.0, 2.5
Maria F , 1, -9.5, 0.0, -4.0, 2.5, 0.0, 0.5
Carlos G , 2, 5.0, 4.5, 0.0, 0.0, -0.5, 0.0
Anastasia, 2, 9.0, 1.0, -2.5, -4.0, 3.5, 0.5
Pablo R , 2, 0.0, -4.0, 0.0, -1.5, 2.0, 2.0

Archivos de salida

juvenil.txt

Jesus M 200
Luis O 125
Maria F 125
Porcentaje en el centro: 0.00%
Promedio de puntos: 150.00

mayores.txt

Marcos P 150
Carlos G 200
Anastasia 0
Pablo R 75
Porcentaje en el centro: 50.00%
Promedio de puntos: 106.25
'''


def leer_participante(registro):
    ''' Subprograma de lectura de los puntos
    '''
    linea = registro.split(',')
    nombre = linea[0]
    categoria = int(linea[1])
    x1 = float(linea[2])
    y1 = float(linea[3])
    x2 = float(linea[4])
    y2 = float(linea[5])
    x3 = float(linea[6])
    y3 = float(linea[7])
    return nombre, categoria, x1, y1, x2, y2, x3, y3


def dentro(x: float, y: float, r: int):
    '''Subprograma que verifica si un punto esta dentro o fuera de un
    circulo con centro en el origen
    '''
    return x ** 2 + y ** 2 <= r ** 2


def puntaje(x: float, y: float, r1: int, r2: int, r3: int):
    ''' Subprograma que determina el puntaje conseguido por un disparo
    '''
    puntaje = 0
    if dentro(x, y, r1):
        puntaje = 100
    elif dentro(x, y, r2):
        puntaje = 50
    elif dentro(x, y, r3):
        puntaje = 25
    return puntaje


def imprimir(arch, nom, punt):
    ''' Subprograma de impresion al archivo de datos
    '''
    arch.write(f'{nom} {punt}\n')


def main():

    # Que tengo?
    nom: str       # Nombre del participante
    cat: int       # Categoria del participante
    x1: float
    y1: float      # Coordenadas del primer disparo
    x2: float
    y2: float      # Coordenadas del segundo disparo
    x3: float
    y3: float      # Coordenadas del tercer disparo

    # Que quiero?
    punt: int       # Puntaje obtenido
    porj: float
    promj: float # Porcentaje y promedio de los juveniles
    porm: float
    promm: float # Porcentaje y promedio de los mayores

    # Variables Auxiliares
    cj: int = 0      # Contador de participantes juveniles
    acumj: int = 0   # Acumulador de puntajes juveniles
    ccj: int = 0     # contador de juveniles que dieron en el centro
    cm: int  = 0     # Contador de participantes mayores
    acumm: int = 0   # Acumulador de puntajes mayores
    ccm: int   = 0   # contador de mayores que dieron en el centro

    # Manejo de archivos
    arch1 = open("principiantes.txt", "r")
    arch2 = open("juvenil.txt", "w")
    arch3 = open("mayores.txt", "w")

    # Ciclo de lectura
    for registro in arch1:
        print(registro)
        nom, cat, x1, y1, x2, y2, x3, y3 = leer_participante(registro)
        print(nom,cat,x1,y1,x2,y2,x3,y3)
        # Clasificacion por categoria
        if cat == 1:
            # calculos e impresion para la categoria juvenil
            punt = puntaje(x1, y1, 2, 4, 6) + puntaje(x2, y2, 2, 4, 6) + puntaje(x3, y3, 2, 4, 6)
            acumj += punt
            cj += 1
            imprimir(arch2, nom, punt)

            # Verificación de que el disparo dio al centro es decir circunferencia de radio 0
            if dentro(x1, y1, 0) or dentro(x2, y2, 0) or dentro(x3, y3, 0):
                ccj += 1
        else:
            # cálculos e impresión para la categoria juvenil
            punt = puntaje(x1, y1, 1, 2, 3) + puntaje(x2, y2, 1, 2, 3) + puntaje(x3, y3, 1, 2, 3)
            acumm += punt
            cm += 1
            imprimir(arch3, nom, punt)

            # Verificación de que el disparo dió al centro es decir circunferencia de radio 0
            if dentro(x1, y1, 0) or dentro(x2, y2, 0) or dentro(x3, y3, 0):
                ccm += 1

    # Cálculos para la Estadistica final de los archivos
    promj = acumj / cj
    porj = ccj * 100 / cj
    promm = acumm / cm
    porm = ccm * 100 / cm

    # Impresiones finales a los archivos
    arch2.write("Porcentaje en el centro: %.2f %%\n" %  porj)
    arch2.write("Promedio de puntos: %.2f\n" % promj)
    arch3.write("Porcentaje en el centro: %.2f %%\n" % porm)
    arch3.write("Promedio de puntos: %.2f\n" % promm)

    # Cierre de archivos
    arch1.close()
    arch2.close()
    arch3.close()

    # Mensaje al usuario
    input("Pulse una tecla para finalizar")

if __name__ == "__main__":
    main()
