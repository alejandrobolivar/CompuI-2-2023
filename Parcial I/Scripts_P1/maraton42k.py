'''
Anualmente se realiza en la ciudad de caracas El Maratón más importante de
Venezuela, al cual se invitan corredores de todo el mundo, y en especial de
América Latina, dicho maratón consiste en un recorrido de 42 kilómetros en una
ruta preestablecida en la ciudad. En este sentido, se desea llevar un registro
sobre la información de sus participantes en la competencia, para lo cual se
tiene:
Nombre, País de procedencia, Género, Tiempo en HORAS-MINUTOS-SEGUNDOS en realizar el recorrido y Kilómetros alcanzados.
Realice un programa que con la información registrada que permita determinar en imprimir por consola
lo siguiente:
Por cada corredor
1) Mensaje que indique si terminó o no el recorrido.
2) Mensaje que muestre Tiempo en segundos en que realizó el recorrido.
Para todos los corredores
3) Nombre y país de los corredores que llegaron de primer y segundo lugar, en caso de haber empate en el
primer lugar debe indicarlo.
4) Nombre del corredor que completo el recorrido y llegó de último.
5) Tiempo promedio en horas-minutos-segundos en que los corredores de Venezuela completaron el
recorrido.
Consideraciones
 Se considera que completó el recorrido el participante cuyos kilómetros alcanzados sea igual a 42
 El género se considera “F” para Femenino y “M” para Masculino.

'Entrada
nombre
pais
genero
hh, mm, ss
kilometros

'Salida
tiempoTotal
nombrePrimerLugar
paisPrimerLugar
nombreSegundoLugar
paisSegundoLugar
nombreEmpate
paisEmpate
nombreUltimo
promedio As Single
hhPromedio, mmPromedio, ssPromedio

'Proceso
cent
tiempoPrimerLugar
tiempoSegundoLugar
primerLugar, segundoLugar, empate, ultimo As Boolean
tiempoUltimo
tiempoVenezuela
contador
'''

# Inicializaciones
cent = "S"
bandera = True
empate = False
segundolugar = False
bandera2 = True
tiempovenezuela = 0
contador = 0
tiempototal = 0
tiempoprimerlugar = 0

# Ciclo de control (lista desconocida)
while cent.upper() == "S":

    # Lectura de datos
    nombre = input("Nombre: ")
    pais = input("País: ")
    genero = input("Genero Masculino (M) ó Femenino (F): ")
    hh = int(input("Horas: "))
    mm = int(input("Minutos: "))
    ss = int(input("Segundos: "))
    kilometros = int(input("Kilómetros: "))

    # Cálculo e impresión del tiempo total de recorrido
    tiempoTotal = hh * 3600 + mm * 60 + ss
    print("2) Tiempo en realizar recorrido: " , tiempototal , " s")

    # Detección del primer y segundo lugar, y verificación de empate
    if kilometros == 42:
        print("1) Terminó el recorrido")

        if bandera:
            nombreprimerlugar = nombre
            paisprimerlugar = pais
            tiempoPrimerlugar = tiempototal
            bandera = False
        elif tiempoTotal <= tiempoPrimerlugar:
            nombresegundolugar = nombreprimerlugar
            paissegundolugar = paisprimerlugar
            tiemposegundolugar = tiempoprimerlugar

            nombreprimerLugar = nombre
            paisprimerLugar = pais
            tiempoprimerLugar = tiempototal

        elif tiempoTotal <= tiemposegundolugar:  # Nuevo segundo lugar
            nombresegundolugar = nombre
            paissegundolugar = pais
            tiemposegundolugar = tiempo

        # Detección del corredor que terminó el recorrido y llegó de último
        if bandera2:
            nombreultimo = nombre
            tiempoultimo = tiempoTotal
            bandera = False
        elif tiempototal >= tiempoultimo:
            nombreultimo = nombre
            tiempoultimo = tiempototal

        # Detección de venezolanos que terminaron el recorrido
        if pais.upper() == "VENEZUELA":
            tiempovenezuela += tiempototal
            contador += 1

    else:
        print("No terminó el recorrido")

    # Pregunta al usuario para saber sí desea añadir más datos
    cent = input("¿Más datos? [S/N]: ")

# Impresión de los ganadores
if bandera: # Validación de existencia de un primer lugar
    print("No hubo ganadores")
else:
    if tiempoprimerlugar == tiemposegundolugar: # Verificación de empate
        print("Hubo empate en el primer lugar")
        print(nombreprimerlugar , " País de procedncia: " , paisprimerlugar)
        print(nombresegundolugar , " País de procedencia: " , paissegundolugar)
    else:
        print("Primer lugar: " , nombreprimerlugar , " País de procedncia: " , paisprimerlugar)
        print("Segundo lugar: ", nombresegundolugar , " País de procedencia: " , paissegundolugar)

# Impresión de corredor que completo el recorrido y llegó de último
if bandera2:
    print("Nadie llegó de último")
else:
    print("Nombre del corredor que completo el recorrido y llegó de último: ", nombreultimo)

if contador != 0:  # Verificación de existencia de un venezolano ganador
    promedio = tiempovenezuela / contador
    # Conversión del tiempo promedio a formato hh/mm/ss
    hhpromedio = promedio // 3600
    mmpromedio = (promedio % 3600) // 60
    sspromedio = (promedio % 3600) % 60
    print("Tiempo promedio (hh/mm/ss) en que los corredores de Venezuela completaron el recorrido: ")
    print(hhpromedio , "/" , mmpromedio , "/" , sspromedio)
else:
    print("Ningún participante venezolano terminó el recorrido")