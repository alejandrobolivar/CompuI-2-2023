# Tabla de multiplicar (del 1 al 10) del número introducido
n = int(input('Tabla: '))
k = 1
while k <= 10:
    print(n,'x',k,'=',n*k)
    k = k + 1
print('Tabla de multiplicar del',n)
