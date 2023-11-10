'''
Mi Red Restaurancito
La última tendencia en cuanto a restaurantes es servir la comida al estilo
 Buffet, donde los clientes pueden servirse lo que deseen en la cantidad que
 deseen. Algunos de ellos utilizan un precio fijo para el plato y otros cobran
 en función del peso que tenga el plato servido. Un restaurante de este estilo,
 que está pronto a inaugurarse, necesita un programa que le ayude en la
 cobranza de los platos servidos, para ello se registran en el archivo
 ventas.txt, los siguientes datos en cada una de las ventas de cada sucursal:

Nombre de la Sucursal y Número de Ventas Realizadas

para cada una de las ventas realizadas:

Nombre del cliente, número de cédula del cliente, peso del plato servido
 (expresado en gramos) y bebida

El dato de la bebida puede tener uno de los siguientes valores:
    "N" = no compró bebida; "S"=Compró Bebida

El programa que debe ser desarrollado en Visual Basic 2008, debe procesar el
 archivo descrito anteriormente, para generar dos archivos compro.txt y
 nocompro.txt, el cual debe contener nombres y cédula de los clientes que
 compraron y no compraron bebidas respectivamente, además determine e imprima
 por pantalla lo siguiente:

Para cada Venta:
a.Para cada venta, monto en BsF. que debe pagar el cliente (comida + bebida)
 incluyendo el IVA.
Para cada Sucursal
b.Porcentaje de clientes que compraron bebida y porcentaje de clientes que no
 compraron bebida
c.Monto promedio cancelado por los clientes que No compraron Bebida
Para la red Restaurancito
d.De los clientes que SÍ compraron bebida, nombre y cédula del cliente que
 canceló más.
e.Ganancia, si por cada plato servido gana el 5% del costo cobrado por del
 mismo y por cada bebida gana el 2%
Consideraciones:
•El IVA se calcula como el 12% del costo del producto adquirido
•El plato servido tiene un precio de BsF. 50,00 por cada 100 gramos de peso
 (NO INCLUYE IVA)
•El precio de las bebidas es: BsF. 8,50 (NO incluye IVA)

# Variables de Entrada
nombresu: str
nombrecl: str
ci: str
nrov: int
peso: float
bebida: str
# Variables de proceso
csic: int
cnoc: int
ct: int
b: int
acumnc: float
montosb: float
montobeb: float
montomayor: float
nombremayor: float
cimayor: str
# Variables de salida
porcentajesc: float
porcentajenc: float
montoprom: float
ganancia: float
monto: float
'''

#  Apertura de los archivos de lectura e impresion
arch1 = open("ventas.txt", 'r')
arch2 = open("compro.txt", 'w')
arch3 = open("nocompro.txt", 'w')

# Inicializacion acumuladores y contadores que se relacionen con informacion de la red restaurancito
ganancia = 0
arch2.write(f"NOMBRE DEL CLIENTE    CI\n")
arch3.write(f"NOMBRE DEL CLIENTE    CI\n")
# Manejo del ciclo de la lista externa
registro = arch1.readlines()
linea = 0

while linea < len(registro):
    lista_ext = registro[linea].split(',')
    linea += 1
    # Lectura de los datos de la lista externa

    nombresu = lista_ext[0]
    nrov = int(lista_ext[1])
    # Inicializacion de acumuladores, banderas, contadores que se relacionen con calculos para cada sucursal
    csic = 0
    cnoc = 0
    acumnc = 0
    b = 0
    print(f"En la sucursal: {nombresu}")
    # Manejo del ciclo que controla lista interna, controlada para el numero de ventas
    for _ in range(nrov):
        lista_int = registro[linea].split(',')
        linea += 1
        nombrecl = lista_int[0]
        ci = lista_int[1]
        peso = float(lista_int[2])
        bebida = lista_int[3].strip('\n')
        # calculo del monto a pagar con IVA, sin bebida
        montosb = (peso * 50 / 100) + (0.12 * (peso * 50 / 100))

        if bebida == "S":
            montobeb = 8.5 + (0.12 * 8.5)  # Monto de la bebida
            monto = montosb + montobeb  # Monto total bebida mas comida
            csic = csic + 1  # Contador de clientes que si compraron bebida
            ganancia = ganancia + ((0.05 * montosb) + (0.02 * (montobeb)))
            arch2.write(f'{nombrecl}                {ci}\n')  # Impresion en el archivo que corresponde a los que si compraron

            if b == 0:  # Calculo de la cliente con mayor monto a pagar, que si haya pedido bebida
                nombremayor = nombrecl
                cimayor = ci
                montomayor = monto
                b = 1
            elif montomayor < monto:
                nombremayor = nombrecl
                cimayor = ci
                montomayor = monto

        else:

            monto = montosb  # Monto total a pagar, ya que no pidio bebida
            cnoc = cnoc + 1  # Contador de cliente que no pidieron bebida
            acumnc = acumnc + monto  # Acumulador de montos de cliente sin bebida, para el promedio
            ganancia = ganancia + (0.05 * montosb)
            arch3.write(f'{nombrecl}               {ci}\n')  # Impresion en el archivo que corresponde a los que no pidieron bebida

        print(f"El monto cancelado por el cliente es de: {monto:.2f} Bs.F")  # Monto cancelado por cada cliente
        # Cierre del ciclo de la lista interna

    ct = cnoc + csic  # Contador total de todos los clientes
    if ct != 0:
        # Calculo de porcentajes
        porcentajenc = (cnoc / ct) * 100
        porcentajesc = (csic / ct) * 100
        print(f"El porcentaje de clientes que no compraron bebida fue de : {porcentajenc:.2f} %")
        print(f"El porcentaje de clientes que si compraron bebida fue de:  {porcentajesc:.2f} %")
    else:
        print("No Hubo clientes")
    
    if cnoc != 0:
        # Calculo de promedio cancelado por clientes que no compraron bebida
        montoprom = (acumnc / cnoc)
        print(f"El promedio cancelado por los clientes que no compraron bebida fue de: {montoprom:.2f} Bs.F")
    else:
        print("No hubo clientes que no compraran bebida")
    
    # Cierre del ciclo de la lista externa

print("Para Mi red restaurancito: ")
if csic != 0:
    print(f"El cliente que cancelo mas dinero, y que comprara bebida fue: El Sr(a). {nombremayor} con CI: {cimayor}")
else:
    print("No hubo clientes que si compraran bebida")

print(f"La ganancia total obtenida fue de : {ganancia:.2f} Bs.F")

# Cierre de los archivos
arch1.close()
arch2.close()
arch3.close()
