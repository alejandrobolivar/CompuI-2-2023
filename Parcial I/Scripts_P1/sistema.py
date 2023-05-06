# Lectura de datos
print('Introduzca los ceficientes: ')
a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))
d = float(input('d:'))
e = float(input('e:'))
f = float(input('f:'))

# Procesamiento de datos
deno = a * e - b * d
if deno == 0:
    # Sí el denominador es cero, no existe solución
    print('No tiene solución el sistema de ecuaciones')
else:
    x = (c * e - b * f) / deno
    y = (a * f - c * d) / deno

# Salida de datos
print('La solución del sistema de ecuaciones planteado es')
print('X=', x)
print('Y=', y)
input('Pulse una tecla para finalizar... ')  # Pausa