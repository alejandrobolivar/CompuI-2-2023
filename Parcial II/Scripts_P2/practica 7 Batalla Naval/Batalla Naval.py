'''batalla naval
El último deseo de Timmy Turner fue jugar Batalla Naval con barcos de
verdad, y sus padrinos mágicos cumpliendo con su deber, se lo
concedieron. Una vez iniciada la batalla Timmy comenzó a disparar misiles
a diestra y siniestra contra la flota enemiga, pero debido a su poca
inteligencia, Timmy no tomaba en cuenta la cinemática del lanzamiento
de proyectiles y a veces acertaba y otras veces no.
Esto obligo a Timmy a desear un ingeniero que lo ayudara con el problema;
como resultado del deseo apareció usted.
El problema es el siguiente: el centro de control del barco de Timmy registra
los siguientes datos sobre los barcos de la flota enemiga:

IDENTIFICACIÓN, DISTANCIA DE DICHO BARCO AL BARCO DE TIMMY (EXPRESADO EN METROS) Y VELOCIDAD INICIAL HORIZONTAL
(VOX) DEL MISIL QUE TIMMY LANZÓ CONTRA ÉL (EXPRESADO EN M/S)

Usted debe desarrollar un programa que lea los datos registrados por el centro de control, en el archivo
lanzamientos.txt usando la teoría del lanzamiento de proyectiles, procese la información y genere dos archivos de
nombre destruidos.txt y nodestruidos.txt, con los números de identificación de los barcos que fueron destruidos y no
destruidos respectivamente.

Adicionalmente determine e imprima por pantalla:
• De los barcos destruidos, la identificación del barco que estaba más cerca.
• De los barcos que NO fueron destruidos, porcentaje de misiles que no alcanzaron al
barco enemigo expresado respecto al total de barcos No destruidos.
• Porcentaje de barcos destruidos.
• Velocidad inicial vertical (V0Y) promedio en m/s.

CONSIDERACIONES
Timmy disparó un misil por cada barco enemigo.
• La velocidad inicial (V0) es un dato proporcionado por el manual del lanzamisiles, el cual
especifica que la velocidad inicial del primer lanzamiento es de 250 m/s, y por cada
nuevo lanzamiento ésta disminuye en 1%.
• Los barcos se considerarán destruidos, si la diferencia entre distancia entre el barco de
Timmy y el barco a destruir almacenada en el archivo y el alcance determinado
mediante la fórmula, es en valor absoluto menor a 10-5

o El misil puede caer antes del barco, en cuyo caso se considera que no alcanzó
el barco, o puede caer después del barco en cuyo caso, se considera que
sobrepasó el barco. En ambos casos el barco se considera NO DESTRUIDO
o No puede agregar centinela al archivo de datos, use la función fin de archivo
o Formulas necesarias:

'''

arch1 = open('lanzamientos.txt','r')
arch2 = open('destruidos.txt','w')
arch3 = open('nodestruidos.txt','w')

# proceso
a = 1
vo = 250
g = 9.80
band = 0
misil = 0
cont = 0
cont1 = 0
suma = 0

for contenido in arch1:
    linea = contenido.split(',')
    
    ident = str(linea[0])
    distancia = float(linea[1])  # en metros
    vox = float(linea[2])  # en metros entre segundo
    
    # calculando alcance, tvuelo, voy 
    
    # importando raiz
    from math import sqrt, fabs
    
    vo = vo * a
    a = 0.99
        
    voy = sqrt(vo**2 - vox**2)  # velocidad vertical
    tvuelo = 2 * voy / g  # tiempo de vuelo
    alcance = vox * tvuelo  # alcance
    
    suma += voy  # sumar las velocidades verticales 
        
    diferencia = distancia - alcance
    
    valor_abs = fabs(diferencia)           
        
    if valor_abs <= 0.001:
        arch2.write(str(ident) + '\n' )  # destruido
        
        if band == 0:
            cerca = ident
            dist_cerca = distancia
            band = 1
        elif distancia < dist_cerca:
            cerca = ident
        
        cont1 += 1 
                    
    else:
        arch3.write(str(ident) +'\n')  # no destruido
        
        cont += 1 
        
        if distancia < alcance:
            # el misil sobrepasa el barco
            print()
        else:       
            misil += 1
            # el misil no alcanza al barco
    
porcentaje = misil / cont *100  # % de misiles que no ALCANZARON los barcos
porce_nodestruidos = cont /(cont+cont1) * 100
vel_prom = suma /(cont+cont1)
    
print('El barco destruido mas cercano es el', cerca, ' a una distancia de %.2f' % dist_cerca, ' m del barco de timmy')
print('el porcentaje de misiles que no alcanzaron a los barcos fue de = %.2f' % porcentaje, ' porciento')
print('el porcentaje de barcos no destruidos con respecto al total de barcos es de = %.2f' % porce_nodestruidos, ' porciento')
print('la velocidad vertical promerdio es de = %.2f' % vel_prom, ' m/s') 
     
arch1.close()
arch2.close()
arch3.close()
