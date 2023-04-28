'''Tres operadores se encargan de realizar mediciones para estimar el peso neto de un producto determinado. Para el registro de las
mismas se cuenta con tres balanzas que utilizan distintas unidades de medición expresadas en kilogramos, gramos y libras
respectivamente. si se conoce cuanto debe pesar cada producto o peso ideal, es posible estimar la cantidad de producto en exceso o
la cantidad de producto faltante expresada en gramos considerando la tabla de equivalencias para realizar las conversiones necesarias
cuando aplique.
Unidad de Medición Equivalencias
Kilogramos kg 1 kg equivales a 1000g
Gramos g -
Libras Ib 1 lb equivale a 0.4536 kg

En el archivo de datos Medidas.txt se registra en la primera línea el Peso ideal del Producto expresado en gramos y en las líneas
siguientes las especificaciones de las mediciones realizadas con:
Número del Operador, Medición Registrada y Unidad de Medición Utilizada (k: kilos; g: gramos; l: libra)

Elabore un programa, que procese la información anterior y genere dos archivos de datos MedidasDesviadas.txt y
MedidasAceptadas.txt que contengan el Número de operador, La Medición Registrada expresada en Gramos y el Porcentaje de
Desviación, con las mediciones desviadas y aceptadas respectivamente, además determine e imprima por consola:
1. Por cada medición realizada, muestre el Número del operador, el Valor de la Medición expresado en gramos y un
Mensaje que indique si la medición es aceptable o no.
2. ¿cuál es El Número del operador, La Medición Registrada y la Unidad de Medición Utilizada que registra el mayor
porcentaje de desviación que ha sido aceptada?'''

arch1 = open('medidas.txt', 'r')
arch2 = open('medidasDesviadas.txt', 'w')
arch3 = open('medidasAceptadas.txt', 'w')

band = 0

pesoideal = float(arch1.readline())

for registro in arch1:
    lista = registro.split(',')
    operador = int(lista[0])
    medida = float(lista[1])
    unidad = str(lista[2].strip('\n'))
    
    if unidad == 'k':
        medicion_gramos = medida * 1000

    elif unidad == 'l':
        medicion_gramos= medida * 0.4536 * 1000
    
    else:
        medicion_gramos = medida
        
    from math import fabs
    
    desviacion = fabs(pesoideal - medicion_gramos) / pesoideal * 100
    
    if desviacion <= 5:
        arch3.write(str(operador) + ' , ' + str(medicion_gramos) + ' , ' + '%.2f ' % (float(desviacion)) + '\n')
    else:
        arch2.write(str(operador) + ' , ' + str(medicion_gramos) + ' , ' + '%.2f' % (float(desviacion)) + '\n')
    
    if band == 0 and desviacion <= 5:
        operador_mayor = operador
        medida_mayor = medida
        unidad_mayor = unidad
        mayor = desviacion
        band = 1

    elif desviacion > mayor and desviacion <= 5:
        operador_mayor = operador
        medida_mayor = medida
        unidad_mayor = unidad
        mayor = desviacion
        
print('mayor desviacion registrada es de: %s, %s, %s' % (operador_mayor, medida_mayor,unidad_mayor) )
        
arch1.close()
arch2.close()
arch3.close()    