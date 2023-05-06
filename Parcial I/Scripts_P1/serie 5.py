'''
'Datos de Entrada
q, r
k
'Datos de Salida
termino
suma
'Variables de proceso
fact
a
i, j
'''
# Lectura de datos por pantalla

k = int(input("Cantidad de términos: "))
q = float(input("Valor de Q: "))
r = float(input("Valor de R: "))

# Inicialización de variables
suma = 0

# Ciclo para generar cada uno de los términos requeridos
for i in range(k):
    # Calculo del factorial
    fact = 1
    for j in range(k-i):
        fact *= j + 1
    # Calculo de A
    a = 0
    for p in range(i+1):
        a += ((-1) ** (p + 2)) * (2 * (p+1) + 3)

    # Cálculo del término correspondiente a cada etapa
    termino = (q ** (2 * k - 1)) / (fact * (r ** a))
    # Suma de cada término
    suma += termino
    # Impresión de cada término
    print("Término ", i, " = ", termino)

# Impresión de la suma total
print("Suma total = ", suma)