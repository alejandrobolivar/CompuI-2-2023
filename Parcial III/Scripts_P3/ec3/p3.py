# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 12:35:53 2022

@author: bolivar

Dado un archivo "datos.txt", lea sus valores e indique cuales valores faltan 
en un rango comprendido desde el menor hasta el máximo valor
"""


def minimo(registro):
    menor = int(registro[0])  # supone menor el primer registro
    for i in registro:
        if int(i) < menor:
            menor = int(i)
    return menor

def maximo(registro):
    mayor = int(registro[0])  # supone mayor el primer registro
    for i in registro:
        if int(i) > mayor:
            mayor = int(i)
    return mayor

def esta(i, registros):
    encontro = False
    j = 0 
    while not(encontro) and j < len(registros):
        if i == int(registros[j]):
            encontro = True
        j +=1
    return encontro

def pregunta1():
    
    arch = open("datos.txt",'r')
    registros = arch.readlines()    
    menor = minimo(registros)
    mayor = maximo(registros)
    for i in range(menor+1, mayor):
        if not(esta(i, registros)):
            print('Falta %d' % int(i))

    print(menor, mayor)
    
pregunta1()
          