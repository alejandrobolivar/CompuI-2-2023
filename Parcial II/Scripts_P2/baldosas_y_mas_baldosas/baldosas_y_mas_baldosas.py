'''
BALDOSAS Y MÁS BALDOSAS (Lista de Lista con manejo de archivos)
En el archivo de datos ordenes.txt se tiene la información que se registra diariamente de las órdenes
de compra de una empresa que distribuye cajas de baldosas para piso. Cada orden de compra
contiene la siguiente información: Número de la orden, Nombre del cliente y varios renglones de
especificaciones: Área a cubrir [m2], dimensiones de la baldosa deseada (largo y ancho [cm]) y
precio por caja de la baldosa deseada.
Cada vez que se procesa una orden de compra se tiene en cuenta las siguientes normativas de la
empresa:

1)El área a cubrir debe aumentarse en 10% para permitir los recortes necesarios para la
colocación de la baldosa
2)Cada caja de baldosa contiene 12 baldosas
3)Solamente se venden UNIDADES completas de cajas; tenga cuidado con el manejo de
enteros y reales

Considerando que usted conoce el número de órdenes que se procesan en un determinado día y el
número de renglones que conforman cada compra, diseñe una aplicación consola que determine y
muestre en el archivo de resultados respuestas.txt lo siguiente:

1)Cada vez que cambie de orden de compra: imprimir una línea formada por 40 guiones
2)Para cada renglón de especificaciones: Número de cajas de baldosas y monto a cancelar
por ese concepto
3)Para cada orden: Monto total a cancelar
4)Al final indique: el número correspondiente a la orden de compra que contiene el menor
número de renglones de especificación

# VARIABLES DE ENTRADA
n As Integer # Ordenes de compras en el archivo
noc As Integer # Indica el numero de la orden de compra
nombre As String # Nombre del cliente
m As Integer # Renglones de especificacion por cada orden de compra
area As Single # Area a cubrir
l, a As Single # Largo y ancho de la baldosa
monto As Single # Monto por caja

# VARIABLES AUXILIARES
band As Integer # Bandera
fc As Integer # Factor de comparacion
# VARIABLES DE SALIDA
monto_total As Single
cancelar As Single
cajas As Integer
mr As Integer # Guarda el numero de orden de menor especificacion
'''

arch2 = open('respuestas.txt','w')
arch1 = open('ordenes.txt','r')
contenido = arch1.readlines()
n = int(contenido[0])  # cantidad de elementos de la lista externa
linea = 1  # Posición del primer elemento de la lista externa
band = 0

for i in range(n):  # CICLO QUE PROCESA LAS ORDENES DE COMPRA (lista externa)
    # LECTURA DE LAS ORDENES
    listaext = contenido[linea].split(',')
    linea += 1  # se incrementa el contador de líneas de contenido
    noc = int(listaext[0])
    nombre =  listaext[1]
    m = int(listaext[2])  # cantidad de elementos de la lista interna
    monto_total = 0.0

    for j in range(m): # CICLO QUE PROCESA LOS RENGLONES DE ESP (lista interna)
        listaint = contenido[linea].split(',')
        linea += 1  # se incrementa el contador de líneas de contenido
        area = float(listaint[0])
        l = float(listaint[1])
        a = float(listaint[2])
        monto = float(listaint[3])

        area = area * 1.1 # Aumento del area en un 10%

        cajas = 1
        while (l * a * 12) * cajas < area:  # Determinación de la cantidad de cajas
            # Mientras que lo que se puede cubrir con las cajas es menor que
            # el área a cubrir, aumente el número de cajas
            cajas += 1 # Contador de cajas

        cancelar = monto * cajas  # Determinacion del monto a cancelar
        monto_total += cancelar #  Determinación del monto total
        arch2.write("N° cajas= " + str(cajas) + " Monto= " + str('%.2f' % cancelar) + '\n')

    arch2.write("Monto Total= "  + str('%.2f' % monto_total) + '\n')

    for w in range(40):  # impresion de los 40 guiones
        arch2.write("-")
    arch2.write('\n')

    if band == 0: # Orden de compra con el menor numero de renglones de especificacion
        band = 1
        fc = m
        mr = noc
    elif fc > m:
        fc = m
        mr = noc

arch2.write("El número de orden con menor cantidad de esp. es: " + str(mr))

arch1.close()
arch2.close()
