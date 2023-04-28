'''

Después de 6 temporadas esta emblemática serie LOST llega a su finaI, lo cual
se ha convertido en todo un acontecimiento mundial, por esta razón, la cadena
ABC creó un concurso para que los fanáticos ganen premios, entre ellos viajar
a USA para conocer a los personajes. Dicho concurso consiste en enviar
mensajes al número LOST, y dependiendo de la cantidad de mensajes enviados se
entregan los premios. Para determinar los ganadores, se tiene en el archivo
fanaticos.txt la siguiente información:
País de procedencia y número de participantes
y para cada participante:
Nombre del participante, edad, cantidad de mensajes enviados
Ante esta situación, la ABC, lo llama a usted, que es un excelente estudiante
de la materia de computación 1 de la facultad de ingeniería de la UC para que
desarrolle una aplicación de consola de VB2008 que determine e imprima por
pantalla:

1.	Nombre, edad y país de procedencia del participante que va a viajar a USA
para conocer al elenco de LOST.
2.	Nombre del primer participante de 23 años que envió más de 10 mensajes.
3.	Promedio de mensajes enviados por los participantes de cada país.
4.	País que cuenta con la menor cantidad de participantes.
Consideraciones:
• El participante que viajara a USA es el que envió la mayor cantidad de
mensajes.

'''


# LOST
# Lista de listas    Interna: conocida    Externa: desconocida


# Variables de entrada
pais: str  # Pais de Procedencia
participantes: int  # Cantidad de participantes por pais
nombre_participante: str  # Nombre de cada participante
edad: int  # Edad de cada participante
cantidad_mensajes: int  # Mensajes enviados por cada participante

# Variables de Salida
nombre_ganador: str  # participante que envió la mayor cantidad de mensajes
edad_ganador: int  # edad del participante que envióa mas mensajes
pais_ganador: str  # Pais de procedencia del que envió mas mensajes
nombre_primero: str  # Nombre del primero de 23 años que envió más de 10 mens
promedio_mensajes_por_pais: float  # Promedio de mensaje enviados por cada pais
pais_menor_cantidad: str  # Pais con la menor cantidad de participantes


# Variables de Proceso
bandera_ganador: bool  # participante ganador
mayor_cantidad_mensajes: int  # Variable para comparar y calcular el ganador
bandera_primero: bool  # primer participante de 23 en enviar mas de 10 mensajes
acumulador_mensajes_por_pais: int  # promedio de mensajes por cada pais
bandera_pais: int  # pais con menor cantidad de participantes
menor_cantidad_participantes: int  # menor cantidad de participantes


# Apertura de archivo
arch1 = open("fanaticos.txt", 'r')

# Inicializacion de Herramientas referentes a todos los paises
bandera_pais = 0
bandera_ganador = 0
bandera_primero = True

registro = arch1.readlines()
linea = 0

while linea < len(registro):
    # Lectura referente a cada pais
    lista_ext = registro[linea].split(',')
    linea += 1

    pais = lista_ext[0]
    participantes = int(lista_ext[1])

    # Cálculo del pais con menor cantidad de participantes
    if bandera_pais:

        pais_menor_cantidad = pais
        menor_cantidad_participantes = participantes
        bandera_pais = 1

    elif participantes < menor_cantidad_participantes:

        pais_menor_cantidad = pais
        menor_cantidad_participantes = participantes

    # Inicializacion de Herramientas para el cálculo del prom de mens por pais
    acumulador_mensajes_por_pais = 0

    # Ciclo referente a la lista interna (Participantes)
    for _ in range(participantes):
        # Lectura de datos de los participantes
        lista_int = registro[linea].split(',')
        linea += 1
        nombre_participante = lista_int[0]
        edad = int(lista_int[0])
        cantidad_mensajes = int(lista_int[0])

        # Acumulador para Cálculo del promedio de mensajes por cada pais
        acumulador_mensajes_por_pais += cantidad_mensajes

        # Cálculo del ganador del concurso
        if bandera_ganador:

            # Captura del primer participante
            nombre_ganador = nombre_participante
            edad_ganador = edad
            pais_ganador = pais
            mayor_cantidad_mensajes = cantidad_mensajes
            bandera_ganador = False

        elif cantidad_mensajes > mayor_cantidad_mensajes:

            # Comparacion para el cálculo del ganador
            nombre_ganador = nombre_participante
            edad_ganador = edad
            mayor_cantidad_mensajes = cantidad_mensajes
            pais_ganador = pais

        # Cálculo del primer participante de 23 años en enviar mas de 10 mensaj
        if bandera_primero and edad == 23 and cantidad_mensajes > 10:

            nombre_primero = nombre_participante
            bandera_primero = False

    # Cálculo del promedio de mensajes enviados por cada pais
    if participantes > 0:
        promedio_mensajes_por_pais = acumulador_mensajes_por_pais / participantes
        print(f"Promedio de mensajes enviados de {pais} = {promedio_mensajes_por_pais:.2f}")

# Impresion de Resultados para todos los paises
print("Ganador del concurso LOST")
print(f"Nombre: {nombre_ganador}  Edad: {edad_ganador} Pais de Procedencia: {pais_ganador}")

if not(bandera_primero):
    # Hubo una persona de 23 años que envió mas de 10 mensajes
    print(f"Nombre del participante de 23 años en enviar mas de 10 mensajes: {nombre_primero}")
else:
    print("No hubo personas de 23 años con mas de 10 mensajes")

print(f"Pais con menor cantidad de mensajes: {pais_menor_cantidad}")

print("_______________________________")
print("Pulse una tecla para finalizar")

# Cierre de archivos
arch1.close()