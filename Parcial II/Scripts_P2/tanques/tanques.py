'''
Una empresa fabricadora de tanques de agua para el consumo humano, 
ha decidido automatizar el control de ventas de sus productos, 
en sus tres presentaciones especiales que tienen forma:  cilíndrica, esférica y de cubo; 
todo esto motivado por la necesidad de los clientes, en cuánto a la selección de la forma 
y tamaño del tanque requerido para la vivienda. Para ello la empresa dispone de un listado 
de clientes en un archivo de nombre “tanques.txt” con la siguiente información de los pedidos:
Por cada cliente se conoce:
El nombre del cliente y la cantidad de tanques requeridos.
Y para cada uno de los tanques se conoce
La forma (1: cilíndrica, 2: esférica, 3 cubo), las dimensiones (m) dependiendo de la forma, y el color.
Desarrolle un programa tipo Aplicación de Consola VB.NET que procese la información anterior y determine e imprima por consola:

Para cada tanque:
1.	Volumen del tanque (m3). (2pto)
2.	Costo del tanque en Bs. (1 pto)

Para cada cliente:
3.	Cantidad de tanques de más de 100 litros solicitados. (1pto)
4.	Promedio del volumen (litros) en tanques cilíndricos. (2pto)

Para todos los pedidos:
5.	Nombre del cliente que realizó la mayor compra, en caso de haber más de uno con el mismo monto indique cuántos. (2ptos)
Consideraciones:

•	Las dimensiones básicas en metros, según la forma son: para el cilíndrico, el radio y la altura; para el esférico, el radio; y para el cubo, un lado.
•	El tanque cilíndrico cuesta 100 Bs/m3, el esférico 150 Bs/m3 y el cubo 50 Bs/m3.
•	1 m3 = 1000 litros.
•	El volumen de una forma esférica es Vesfera = (4/3) π r3, para una forma cilíndrica es Vcilindro = π r2 h y para una forma de cubo Vcubo = l3
•	El valor de  se obtiene mediante la función Math.Pi.
•	Ejemplo del archivo de dato “tanques.txt”.

'''
from math import pi
cont_cil = 0
suma_vol_cil = 0
precio = [100, 150, 50]  # Bs/m3
c_100 = 0
band = True
arch = open('tanques.txt', 'r')

while True:
    linea = arch.readline()
    
    if linea == '':  # Fin del archivo
        break
    
    else:
        lista_ext = linea.split(',')
        nombre = lista_ext[0]
        cant_tanques = int(lista_ext[1])
        print(f'Cliente: {nombre}')
        print(f'Cantidad de tanques: {cant_tanques}')
        total_compra = 0
        
        for _ in range(cant_tanques):
            lista_int = arch.readline().split(',')
            forma = int(lista_int[0])
            
            if forma == 1:  # cilíndrico
                r = float(lista_int[1])
                h = float(lista_int[2])
                color = lista_int[3].strip('\n')
                vol = pi * r**2 * h
                cont_cil += 1
                suma_vol_cil += vol * 1000  # litros
            elif forma == 2:  # esférico
                r = float(lista_int[1])
                color = lista_int[2].strip('\n')
                vol = 4/3 * pi * r**3
            else:  # cubo
                l = float(lista_int[1])
                color = lista_int[2].strip('\n')
                vol = l ** 3
            print(f'Volumen del tanque= {vol:.2f} m3')
            costo = vol * precio[forma-1]
            print(f'Costo del tanque= {costo:.2f} Bs')
            total_compra += costo
            
            if vol*1000 > 100: 
                c_100 += 1
            
            if band:
                nombre_mayor = nombre
                compra_mayor = total_compra
                cont_igual = 0
                band = False
            elif total_compra > compra_mayor:
                nombre_mayor = nombre
                compra_mayor = total_compra
            elif total_compra == compra_mayor:
                cont_igual += 1

if c_100 != 0:
    print(f'Se solicitarón {c_100} tanques de más de 100 litros')
else:
    print('No Se solicitarón tanques de más de 100 litros')

if cont_cil !=0:
    promedio_cil = suma_vol_cil / cont_cil
    print(f'Promedio del volumen en tanques cilindricos {promedio_cil:.2f} litros')
else:
    print('No hubo tanques cilíndricos')
    
if band:
    print('El archivo está vacío')
elif cont_igual == 0:
    print(f'{nombre_mayor} fué el cliente con la mayor compra')
elif cont_igual > 0:
    print(f'{nombre_mayor} fué el cliente con la mayor compra y hubo {cont_igual} clientes con el mismo monto de la mayor compra')
    
arch.close()