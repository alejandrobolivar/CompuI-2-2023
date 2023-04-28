# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:21:37 2022

@author: bolivar
Validar y devolver un número entero x entre a y b; guardelo en un archivo datos.txt
Leer n valores.
"""

def pregunta1():
    arch = open("datosn.txt",'w')
    
    n = int(input("n:"))
    a = int(input("a:"))
    b = int(input("b:"))
    cont = 0
    while cont < n:
        x = int(input("x:"))
        if a <= x <= b:
            arch.write("%d\n" % x)
            cont += 1

pregunta1()
            
    