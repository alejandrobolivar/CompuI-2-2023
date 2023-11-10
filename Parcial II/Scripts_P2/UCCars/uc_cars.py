'''
Una compañía ensambladora de automóviles está realizando pruebas
de eficiencia a los diferentes modelos de autos que ensambla. Estas
pruebas consisten en subir el auto a velocidad constante por varias
colinas con diferentes ángulos de elevación (alfa).
Los resultados de dichas pruebas se utilizan para calcular el porcentaje
de eficiencia del auto, de acuerdo a la siguiente expresión:

Eficiencia[%] = consumo teórico de gasolina [L] * 100 / consumo real de gasolina [L]

Para ello, la compañía ensambladora registra en un archivo de datos de nombre pruebas.dat, la siguiente
información del auto:
Modelo, Masa del auto (kg), Eficiencia mínima aceptable (%), Número de pruebas
Y para cada auto se registra la información de las pruebas realizadas:
Angulo de la colina (grados), Distancia recorrida (m), Consumo real de gasolina en el recorrido (L)
En vista de su altísimo rendimiento en la materia Computación I, usted fue seleccionado para que
desarrolle un programa en Pascal que lea la información del archivo de datos pruebas.dat y determine e
imprima en un archivo de datos de nombre aprobados.dat, los siguientes datos de los modelos que pasan
la prueba de subir colinas:
Modelo, Eficiencia mínima aceptable (%), Eficiencia promedio obtenida (%)
Además se pide que imprima por pantalla lo siguiente:
• Modelo del auto y ángulo de elevación de la prueba con menor eficiencia.
• Porcentaje de autos que pasaron la prueba.
CONSIDERACIONES:
• Un auto pasa las pruebas de subir colinas si el promedio de las eficiencias obtenidas en las pruebas es mayor a la
eficiencia mínima aceptable del auto.
 consumo teórico de gasolina [L] = Trabajo para subir el automóvil [Joule] / Calor de combustión de la gasolina[Joule/L]
• 180° = pi rad
• La función interna de pascal que calcula el seno se escribe sin(x), donde x es el valor o la expresión del que
desean obtener el valor del seno, debe estar en radianes.

# Variables de Entrada
modelo: str                    # Modelo del auto registrado
peso: float                      # Peso del Auto
EficienciaMinimaAceptable: float # Eficiencia minima aceptable del auto registrado
NumeroDePruebas: int          # Numero de pruebas realizadas para un modelo
Angulo: float                    # Angulo de inclinacion de la colina en la prueba
DistanciaRecorrida: float        # Distancia recorrida durante la prueba en metros
ConsumoRealGasolina: float       # Consumo real de gasolina en litros
# Variables de Proceso
Eficiencia: float                # Eficiencia calculada de la prueba
ModeloMinimaEficiencia: str = ""    # Modelo con menor eficiencia en una prueba
# Variables de Salida
AcumuladorDeEficiencias: float   # Acumulador de las eficiencias de las pruebas de un mismo auto
MinimaEficiencia: float          # Menor eficiencia registrada
AnguloDeMinimaEficiencia: float  # Angulo de inclinacion de la colina en la prueba con menor eficiencia
ContadorDeAutos: int          # Contador del total de autos registrados en el archivo
ContadorDeAutosAprobados: int # Contador del autos aprobados registrados
Bandera: int                  # Bandera
'''
import math
# Inicializacion de la bandera
Bandera = 0
ContadorDeAutos = 0
ContadorDeAutosAprobados = 0

# Apertura de archivos
arch1 = open("pruebas.txt", 'r')
arch2 = open("aprobados.txt", 'w')

# Ciclo hasta el fin de archivo 1, lista externa
while True:
    # Lectura de datos de un modelo
    linea = arch1.readline()
    if linea == '':
        break

    reg = linea.split(',')

    modelo = reg[0]
    peso = float(reg[1])
    EficienciaMinimaAceptable = float(reg[2])
    NumeroDePruebas = int(reg[3])

    # inicializacion del acumulador de eficiencias de un mismo modelo
    AcumuladorDeEficiencias = 0

    # Ciclo determinado, del numero de pruebas realizadas, lista interna
    for _ in range(NumeroDePruebas):

        # Lectura de datos de la prueba
        linea = arch1.readline()
        reg = linea.split(',')
        Angulo = float(reg[0])
        DistanciaRecorrida = float(reg[1])
        ConsumoRealGasolina = float(reg[2])

        # Calculo de la eficiencia de una prueba
        Eficiencia = ((peso * DistanciaRecorrida * 9.8 * math.sin(Angulo * math.pi / 180)) / 3200) / ConsumoRealGasolina * 100

        # Acumulacion de las eficiencias de las pruebas de un mismo modelo
        AcumuladorDeEficiencias += Eficiencia

        # Determinacion de la prueba con la menor eficiencia
        if Bandera == 0:
            # Obteniendo un valor inicial para la comparacion
            MinimaEficiencia = Eficiencia
            ModeloMinimaEficiencia = modelo
            AnguloDeMinimaEficiencia = Angulo
            Bandera = 1
            # Comparacion de eficiencias
        elif MinimaEficiencia > Eficiencia:
            MinimaEficiencia = Eficiencia
            ModeloMinimaEficiencia = modelo
            AnguloDeMinimaEficiencia = Angulo

        # Fin del ciclo para las pruebas de un modelo

    # Contando el total de autos registrados
    ContadorDeAutos += 1

    # Determinando si el carro fue aprobado
    if (AcumuladorDeEficiencias / NumeroDePruebas) > EficienciaMinimaAceptable:
        # Impresion de aprobados en el archivo 2
        arch2.write(f'{modelo}, {EficienciaMinimaAceptable}, {AcumuladorDeEficiencias / NumeroDePruebas:.2f}')
        # Contando los autos aprobados
        ContadorDeAutosAprobados += 1

# Fin del ciclo del archivo

# Cerrando ambos archivos
arch1.close()
arch2.close()

# Impresion de resultados por consola
print(f"El modelo con menor eficiencia fue {ModeloMinimaEficiencia} en la prueba con {AnguloDeMinimaEficiencia} °, con {MinimaEficiencia:.3f} % de eficiencia")

# Validacion de existencia de autos aprobados
if ContadorDeAutosAprobados == 0:
    print("No se registraron autos aprobados")
else:
    print(f'El porcentaje de aprobados fue de {ContadorDeAutosAprobados * 100 / ContadorDeAutos:.3f} %')
