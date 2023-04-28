# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:42:08 2022

@author: bolivar
Dados dos archivos a.txt y b.txt que contienen números enteros, devuelva un 
archivo union.txt con los números de ambos archivos, interseccion.txt 
con los números repetidos en ambos archivos y otro diferencia_simetrica.txt  
con los números no comunes en ambos archivos.

"""

def union(registro1, registro2, arch):
    
    for i in registro1:
        arch.write("%d\n" % int(i))
    for i in registro2:
        arch.write("%d\n" % int(i))

def es_repetido(i, registro2):
    band = False
    j = 0
    while j <= len(registro2) and not(band):
        if int(i) == int(j):
            band = True
        else:
            j += 1
    return band
    
def interseccion(registro1, registro2, arch):
    for i in registro1:        
        if es_repetido(i, registro2):
            arch.write("%d\n" % int(i))


def diferencia_simetrica(registro1, registro2, arch):
    
    for i in registro1:      
        if not(es_repetido(i, registro2)):
            arch.write("%d\n" % int(i))


def pregunta4():
    
    arch1 = open("a.txt",'r')
    arch2 = open("b.txt",'r')
    arch3 = open("union.txt",'w')
    arch4 = open("interseccion.txt",'w')
    arch5 = open("diferencia_simetrica.txt",'w')
    
    registros_a = arch1.readlines() 
    registros_b = arch2.readlines()     
    
    union(registros_a, registros_b, arch3)
    interseccion(registros_a, registros_b, arch4)
    diferencia_simetrica(registros_a, registros_b, arch5)
    
    arch1.close()
    arch2.close()
    arch3.close()
    arch4.close()
    arch5.close()

pregunta4()
    