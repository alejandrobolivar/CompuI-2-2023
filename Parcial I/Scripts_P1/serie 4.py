'''
'Variables de Entrada
q
x
z
'Variables de Salida
s ' Variable que acumulará los términos
t ‘ Término
'Variables de Proceso
i, j 'variables del ciclo
f ' variable que almacena el factorial
num, den
'''

# Lectura de variables
q = int(input("Introduzca la cantidad de términos: "))
x = float(input("Introduzca el valor de X: "))
z = float(input("introduzca el valor de Z: "))

# Inicialización de variables
s = 0
# Ciclo para la serie
for i in range(q):
    # Cálculo del factorial
    factorial = 1
    for j in range(q + i):
        factorial *= j + 1

    # Forma de generar la alternabilidad del signo
    if i % 2 == 0:  # Término par y negativo
        num = -factorial
        den = x ** (q + i) * z ** (2 * i + 1)
    else:  # Término impar y positivo
        num = (x ** 3) * factorial
        den = z ** (2 * i + 1)

    t = num / den
    print("El término ", i, " es: ", t)
    # Se acumula cada término
    s += t

print("El valor de la sumatoria es: ", s)