'''
'Variables de Entrada
x
y
n
'Variables de Salida
t
s
'Variables de Proceso
den
num
signo
i
'''

# Inicialización
signo = -1
s = 0
# Proceso y salida de datos

x = float(input("x: "))
y = float(input("y: "))
n = int(input("n: "))

for i in range(n):

    factorial=1
    for j in range(2 * i + 3):
        factorial *= j + 1

    if i % 2 == 0:
        num = factorial * y ** (n - i)
        den = x ** (3 * (i + 1))
    else:
        num = x ** (3 * (i + 1))
        den = factorial * y ** (n - i)

    t = signo * num / den
    print("Término= ", t)
    s += t
    signo = 1

print("Suma= ", s)