# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:04:02 2022

@author: bolivar

Devuelva la cantidad de digitos en cada número contenido en un archivo datos.txt
"""

def cant_digitos(x):
    
    aux = x
    c = 0
    while aux > 0:
        aux = aux //10
        c += 1
    return c

def pregunta2():
    
    arch = open("datos.txt",'r')
    registros = arch.readlines()    # ['5\n', '9\n', '4\n', '2\n', '8\n', '20']

    for i in registros:
        print('%d tiene %d' % (int(i), cant_digitos(int(i))))


pregunta2()