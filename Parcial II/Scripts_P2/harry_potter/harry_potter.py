'''
Ya está a la venta los tickets del estreno de la película “Harry Potter y el
Príncipe Mestizo – La historia de Riddle” en la Sala Premium de Cines Montaña.
Para esto, en una lista, se anota el número del ticket, el número de fila (1 a 11)
y la letra de la columna del asiento (De la A a la L). Se conoce que los asientos
de las filas 1-5 cuestan $20; los asientos de las filas 6-8 cuestan BsF. 30 y los
asientos de las filas 9-11 cuestan BsF 17. Desarrolle un programa que lea la
información de la lista que se encuentra almacenada en el archivo de nombre
datos.txt y determine e imprima por pantalla:
a. Número del ticket y fila de la primera persona que compró el primer
ticket en un asiento de la columna F y cuantos después de él se
sentaron en la misma fila.
b. Total de BsF recaudado por venta de tickets.

# Variables de entrada
ticket: int
fila: int
columna: str
# Variables de salida
ticketprimero: int
filaprimero: int
contadorf: int
total: float
# Variables de proceso
primero: bool  # bandera para determinar el primero en sentarse en la columna F
'''

# Apertura del archivo
arch = open("Datos.txt", 'r')
primero = True
contadorf = 0
total = 0

for registro in arch:
    linea = registro.split(',')

    # Lectura de los datos
    ticket = int(linea[0])
    fila = int(linea[1])
    columna = linea[2].strip('\n')
    # Calculo de cual fue la primera persona que se sentó en la columna F
    if ((columna == "F") or (columna == "f")) and primero:  # si está en la columna F y es el primero
        ticketprimero = ticket
        filaprimero = fila
        primero = False
    else:
        # Calculo de cuantos ademas del primero se sentaron en la fila F

        if not primero:  # si tengo el primero que se sentó en la columna F, determino cuantos se sentaron en la misma fila
            if filaprimero == fila:
                contadorf += 1

    if 1 <= fila <= 5:  # de la 1 a la 5
        total += 20
    elif 6 <= fila <= 8:  # de la 6 a la 8
        total += 30
    elif 9 <= fila <= 11:  # de la 9 a la 11
        total += 17

if primero:
    print(" Nadie se sentó en la columna F ")
else:
    print(f" El ticket de la primera persona que se sentó en la columna F fue: {ticketprimero}")
    print(f" y se sentó en la fila: {filaprimero}  ")
    print(f" Además del primero se sentaron en la misma fila: {contadorf}")

print(f" El total recaudado fue: ${total}")

arch.close()
