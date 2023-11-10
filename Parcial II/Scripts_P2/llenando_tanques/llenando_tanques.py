'''
En un complejo residencial, un grupo de vecinos se ven en la necesidad de llenar sus
tanques, en vista que hay serios problemas con el agua. Toda el agua disponible se
encuentra almacenada en un tanque subterráneo del complejo, y para llenar el
resto de los tanques basta con utilizar el agua disponible; pero, para mayor
complicación el caudal de descarga no es lo suficientemente fuerte como para
hacer el llenado utilizando una manguera y no disponen de una bomba hidráulica.
En vista de la situación y la gran necesidad de utilizar el agua, los vecinos toman la
opción de llenar los tanques utilizando tobos.
En un archivo de datos de nombre “RESIDENCIAS.TXT” se encuentra almacenada la siguiente información:
En la primera línea,
VOLUMEN DE AGUA DISPONIBLE EN EL TANQUE SUBTERRÁNEO (m3), CAUDAL INICIAL DE DESCARGA (m3/s)
en las líneas siguientes, por cada tanque a llenar:
NÚMERO DE LA CASA A LA QUE PERTENECE EL TANQUE
y por cada tobo utilizado para llenar los tanques:
TIEMPO DE LLENADO DEL TOBO (s), ESTATUS (0 si no ha llenado el tanque, 1 si lo llena)
Procese la información del archivo “RESIDENCIAS.TXT” y genere dos archivos; “LLENOS.TXT”, donde se almacene el
número de la casa donde su tanque se llenó completamente y cuantos tobos necesitó para lograrlo, y
“RESULTADOS.TXT” donde se imprima:
Para cada tobo:
1. Volumen del tobo en L. ( 1 punto)
Por cada tanque que se logra llenar:
2. Volumen del tanque en m3. (1 punto)
3. Volumen disponible en el tanque subterráneo para llenar el resto de los tanques, expresado en m3. ( 2 puntos)
Para todo el proceso de llenado:
4. Número de la casa en la que el tanque se llenó parcialmente, pues no se llenó completamente por falta de
agua. Y ¿Cuántos tanques se llenaron completamente antes de intentar llenarlo? (2 puntos)
Además imprima por consola:
5. Tiempo promedio de llenado de los tanques que se pudieron llenar por completo en minutos.(2 puntos)
Consideraciones:
 El caudal disminuye un 1% en cada llenado de un tobo y siempre se mantiene por lo menos por encima de cero
m3/s. Al finalizar el llenado de un tanque los vecinos descansan y el caudal para el llenado del siguiente tanque se
recupera, así que vuelve a ser el inicial.
 El volumen de un tobo se determina como: V = Q * t
V: Volumen del tobo (m3),
Q: Caudal (m3/s)
t: tiempo de llenado (s)
 1m3 es el equivalente a 1.000 L.
 60 segundos es el equivalente a 1 minuto.
 El volumen de un tanque se determina como la suma de los volúmenes de todos los tobos utilizados para llenarlo.
 Cuando se acaba el agua disponible ya no se pueden llenar más tobos y por tanto no se llenan más tanques.
 Se llenan los tanques uno por uno. Una vez llenado un tanque se comienza a llenar otro.

# Entradas
VolumenTanque: float
Caudal: float
TiempoLLenado: float
NroCasa: int
Estatus: int

# Salidas
VolumenTanqueCasa: float
VolumenDisponible: float
VolumenTobo: float
NroCasaParcial: int
CantAntesParcial: int
CantTobos: int
Promedio: float

# Procesos
AcumTiempo: float
CaudalAux: float
Tiempo: float
Band: bool
i: int  # Auxiliar
CantAntes: int
'''

# Registro de Archivos
arch1 = open('residencias.txt', 'r')
arch2 = open('llenos.txt', 'w')
arch3 = open('resultados.txt', 'w')

# Zona 1
# Lectura de Datos
linea = arch1.readline()
lista = linea.split(',')
VolumenTanque = float(lista[0])
Caudal = float(lista[1])

# Inicializacion de Herramientas
CantAntes = 0
AcumTiempo = 0
Band = True
VolumenDisponible = VolumenTanque

# Ciclo Externo: Desconocido
while True:

    linea = arch1.readline()
    if linea == '':
        break
    # Zona 2
    # Inicializacion de Heramientas
    CaudalAux = Caudal
    VolumenTanqueCasa = 0
    CantTobos = 0
    i = 0

    # Lectura de Datos
    NroCasa = int(linea)

    while True:
        # Zona 3
        # Lectura de Datos
        linea = arch1.readline()
        TiempoLLenado = int(lista[0])
        Estatus = int(lista[1])

        # Calculos Pertinentes
        if CaudalAux > 0:
            CaudalAux = CaudalAux - CaudalAux * 0.01

        # Volumen del Tobo en L
        VolumenTobo = (TiempoLLenado * CaudalAux) * 1000
        i += 1
        arch3.write(f"Volumen del Tobo Nro {i}: {VolumenTobo}(L)")

        # Cantidad de Tobos que se LLenan
        CantTobos += 1

        # Volumen del Tanque en m^3
        VolumenTanqueCasa += VolumenTobo

        # Volumen Disponible
        VolumenDisponible -= VolumenTobo

        # Acumulador de Tiempo de llenado
        AcumTiempo += TiempoLLenado

        if Estatus == 1 or VolumenDisponible <= 0:
            break

    # Zona 4
    # Calculos e Impresiones
    if Estatus == 1:
        # Contar los tanques que se llenaron antes del parcialmente
        CantAntes += 1

        # Tiempo que duro en LLenarse el Tanque
        Tiempo = AcumTiempo / 60

        # Los que se lograron llenar
        arch2.write(f"Nro de la Casa: {NroCasa}; Necesito: {CantTobos} tobos para llenar el tanque")

        # Volumen del Tanque en m^3
        arch3.write(f"Volumen del Tanque: {VolumenTanqueCasa}(m^3)")

        # Volumen Disponible
        arch3.write(f"Volumen Disponible en el Tanque Subterraneo: {VolumenDisponible}(m^3)")
    elif Band:  # Se asigna el Numero de la casa que el tanque se lleno parcialmente
        NroCasaParcial = NroCasa
        CantAntesParcial = CantAntes
        Band = False

# Zona 5
# Impresion de Resultados
# Nro de la casa y cuantos antes de el
if not Band:
    arch3.write(f"Nro de la Casa: {NroCasaParcial}; La Cantidad de Tanques que se llenaron Completamemnte: {CantAntesParcial}")
else:
    arch3.write("Todos los Taques se Llenaron")


# Tiempo Promedio
if CantAntes != 0:
    Promedio = Tiempo / CantAntes
    print(f"Tiempo Promedio de Llenado es de: {Promedio:.2f} min")
else:
    print("Ningun Tanque se Logro Llenar")

# Control de Cierre
input("====== Pulse Cualquier Tecla Para Cerrar ======")

arch1.close()
arch2.close()
arch3.close()
