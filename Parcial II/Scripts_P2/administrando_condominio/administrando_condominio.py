# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 15:05:54 2022

@author: bolivar
"""
'''
P R E G U N T A # 2 A D M I N I S T R A N D O E L C O N D O M I N I O
La compañía administradora de un edificio de M apartamentos necesita con
urgencia cierta información estadística para la toma de decisiones en cuanto a los
deudores. Por cada apartamento se registró, en archivo de nombre condominio.txt:
Apartamento Nombre del Dueño Meses adeudados Monto adeudado (Bs. F)
Desarrolle un programa que lea la información de los M apartamentos y determine e imprima:
1. Porcentaje de apartamentos que tienen 3 ó mas meses adeudados.
2. Nombre del dueño del apartamento que tiene el menor monto adeudado, sin considerar los que no
tienen deuda.
3. Mensaje que indique si hay algún apartamento sin deuda.
Nota: Si no tiene deuda, su monto adeudado es cero (0).

Variables de entrada
apartamento As String
dueño As String
mesesa, m As Integer
montoa As Single
Variables de salida
dueñomenor As String
porc As Single
Variables del proceso
registro As Integer
meses3 As Integer
band As Boolean
menor As Single
contador As Integer
'''

arch = open("condominio.txt", "r")
band = True
contador = 0
meses3 = 0
contenido = arch.readlines()
m = int(contenido[0])

for registro in range(1, m+1):

    datos = contenido[registro].split(',')
    print(datos)
    apartamento = datos[0]
    dueño = datos[1]
    mesesa = int(datos[2])
    montoa = float(datos[3])

    if mesesa >= 3:
        meses3 += 1

    if montoa != 0:
        if band:
            menor = montoa
            dueñomenor = dueño
            band = False
        else:
            if montoa < menor:
                menor = montoa
                dueñomenor = dueño
    else:
        contador += 1

porc = (meses3 / m) * 100
print("el porcentaje de apartamentos con mas de tres meses adeudados fue %.2f" % porc, "%")

if band:
    print("Todos los apartamentos estan solventes")
else:
    print(f"El dueño del apartamento con menor deuda es: {dueñomenor}")

if contador != 0:
    print("Hay %d apartamento(s) solvente(s)" % contador)
else:
    print(" No hay apartamentos Solventes, estamos en emergencia ")