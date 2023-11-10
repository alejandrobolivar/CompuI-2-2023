'''
Una empresa de trenes desea automatizar las estadísticas de su venta de
pasajes, además de analizar sus ingresos. Para ello en un archivo de nombre
“pasajes.txt” se registran los siguientes datos de los diferentes pasajes vendidos
en sus terminales de trenes, en el mismo se almacena para cada terminal:
Nombre del terminal y número de pasajes vendidos
Y para cada uno de los pasajes vendidos
Numero serial del pasaje, kilómetros que se van a recorrer y cantidad de días que durará el viaje.
Se pide desarrolle un programa que genere un archivo de nombre ingresos.txt, el
cual debe contener Número de Serial de Pasaje, Monto Cancelado
(incluyendo el descuento si aplica) y un mensaje que indique si recibió o no
recibió descuento. Además determine e imprima por pantalla:
1. Numero serial y Nombre del Terminal donde fue vendido el
primer pasaje en recibir descuento que tiene una duración
del viaje menor a 8 días.
2. Por cada terminal, promedio de monto cancelado por los
pasajes que obtuvieron descuento
3. Terminal con mayor ingreso por los pasajes vendidos
Consideraciones:
• El precio de un pasaje en tren se calcula tomando en
cuenta el número de kilómetros que se van a recorrer, siendo el precio 60 BsF/Km
• Este precio puede tener un descuento del 30% si la duración del viaje es de al menos 7 días, ó si el
recorrido supera los 800 Km

# Entradas
NomTerminal: str = ''
CantPasajes: int
NroSerial: int
Kilometros: float
CantDias: int

# Salidas
NroSerialMenor: int
NombTerminalMenor: str = ''
Monto: int
Prom: float
TerminalMayor: str = ''

# Procesos
BandMenor: bool
BandMayor: bool
AcumMonto: int
ContDescuento: int
AcumMayor: int
Descuento: int
MayorIngreso: int
'''

# Registro de Archivos
arch1 = open('pasajes.txt', 'r')
arch2 = open('ingresos.txt', 'w')

# Zona 1: Inicializacion de Herramientas
BandMayor = True
BandMenor = True

# Ciclo Externo
while True:
    # Zona 2
    # Inicializacion de Herraminetas
    AcumMonto = 0
    ContDescuento = 0
    AcumMayor = 0

    # Lectura de Datos
    linea = arch1.readline()
    lista_ext = linea.split(',')
    NomTerminal = lista_ext[0]
    CantPasajes = int(lista_ext[1])

    # Ciclo Interno
    for _ in range(CantPasajes):
        # Zona 3
        # Inicializacion de Herramientas
        Descuento = 0
        # Lectura de Datos
        linea = arch1.readline()
        lista_ext = linea.split(',')
        NroSerial = int(lista_ext[0])
        Kilometros = float(lista_ext[1])
        CantDias = int(lista_ext[2])

        # Calculos internos
        Monto = Kilometros * 60
        # Verifico si hay Descuento
        if CantDias >= 7 or Kilometros > 800:
            Monto = Monto - Monto * 0.3
            Descuento = 1

        # Asigna el primer pasaje con menor dias de viaje
        if CantDias < 8 and Descuento == 1 and BandMenor:
            NroSerialMenor = NroSerial
            NombTerminalMenor = NomTerminal
            BandMenor = False

        # Calculo para el Promedio
        if Descuento == 1:
            AcumMonto += Monto
            ContDescuento += 1

        # Calculo para el mayor Ingreso
        AcumMayor += Monto

        # Impresion de Resultados Para cada Pasaje
        if Descuento == 1:
            arch2.write("Nro de Serial: ", NroSerial, "; Monto a Cancelar: ", Monto, " Si Recibio Descuento")
        else:
            arch2.write("Nro de Serial: ", NroSerial, "; Monto a Cancelar: ", Monto, " No Recibio Descuento")

    # Zona 4: Calculos e Impresion de Resultados Para cada terminal
    # Calculos
    if BandMayor:
        TerminalMayor = TerminalMayor
        MayorIngreso = AcumMayor
        BandMayor = False
    elif AcumMayor > MayorIngreso:
        TerminalMayor = TerminalMayor
        MayorIngreso = AcumMayor

    # Impresiones
    if ContDescuento > 0:
        Prom = AcumMonto / ContDescuento
        print("Promedio de Monto Cancelado es de: ", Prom)
    else:
        print("No hubo Descuento")

# Zona 5: Impresion de Resultados Para Todos
if not BandMayor:
    print(f"El Terminal con mayor ingreso es: {TerminalMayor}")
else:
    print("No hubo algun Terminal con mayor ingreso")

if not BandMenor:
    print("Primer Nro de serial y Nombre del Terminal con descuento y menor duracion de viaje: ")
    print("Nro se Serial: ", NroSerialMenor,  "; Terminal: ", NombTerminalMenor)
else:
    print("No hubo descuento en algun terminal")

arch1.close()
arch2.close()
print("Pulse Cualquier tecla para Cerrar")
