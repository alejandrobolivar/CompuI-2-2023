# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 15:05:09 2022

@author: bolivar
"""
'''
P R E G U N T A # 3 L A I M P O R T A D O R A E N T R E G O B I E N ( 7 P T O S )
En la actualidad la empresa importadora ENTREGO BIEN C.A., piensa
entrar al mercado nacional, para ello requiere que se le elabore un
algoritmo para un programa que se encargue de establecer el costo
por nacionalización de los productos que ellos entregarán a sus
clientes. Para cada producto que entrega se le toma los siguientes
datos: Descripción del producto, tipo de producto (1=Electrónico,
2=Medicina, 3=Alimento, 4=Otros), Costo del producto en Dólares.
El gobierno establece, según sea el tipo del producto, el pago por
nacionalización basado en los siguientes criterios:
a) Si el producto tiene un costo menor a 100$, no paga nacionalización.
b) De ser el costo superior a 100$, el pago por nacionalización se determina 
como un porcentaje del costo del producto y se establece según la siguiente tabla:

    Tipo de producto Pago de Nacionalización
    Electrónico 100% del costo
    Medicina 10% del costo
    Alimentos 10% del costo
    Otros 85% del costo

Se le pide a usted que desarrolle un programa que dada la información antes mencionada, determine e
imprima:
Para cada producto:
• Descripción del producto, pago por nacionalización (BsD.)
Para todos los productos:
• Promedio de costo en dólares de los productos electrónicos importados.
• Porcentaje de Productos de tipo electrónico que no pagan nacionalización con respecto al total de
productos electrónicos importados.
Consideraciones:
1 Dólar = 4.5 BsD.
'

'Variables de entrada
descripcion
tipo
costo
'Variables de salida
pago
por
prom
'Variables de proceso
concosto
conelectronicos
electronicos
'''

# Archivos
arch = open("importaciones.txt", "r")

# inicio de herramientas
concosto = 0
conelectronicos = 0
electronicos = 0

for registro in arch:
    
    contenido = registro.split(',')
    
    descripcion = contenido[0]
    tipo = int(contenido[1])
    costo = float(contenido[2])

    if costo >= 100:
        if tipo == 1:
            pago = (costo + 1 * costo) * 4.5
            concosto = concosto + costo
            conelectronicos = conelectronicos + 1
        elif tipo == 2:
            pago = (costo + 0.1 * costo) * 4.5
        elif tipo == 3:
            pago = (costo + 0.1 * costo) * 4.5
        else:
            pago = (costo + 0.85 * costo) * 4.5

        print("El producto %s tiene un pago por nacionalizacion de %.2f BsD. " % (descripcion, pago))
    else:
        print("El producto %s no paga nacionalización " % descripcion)

        if tipo == 1:
            electronicos = electronicos + 1

if conelectronicos != 0:
    prom = concosto / conelectronicos
    print("El Promedio de costo en dólares de los productos electrónicos importados fue $%.2f  " % prom)
else:
    print("No hubo productos electrónicos importados con un costo mayor a $100")

if (conelectronicos + electronicos) != 0:
    por = (electronicos / (conelectronicos + electronicos)) * 100
    print("El Porcentaje de Productos de tipo electrónico que no pagan nacionalización con respecto al total de productos electrónicos importados fue de %.2f " % por, "%")
else:
    print("No hubo productos electrónicos importados con un costo menor a $100")