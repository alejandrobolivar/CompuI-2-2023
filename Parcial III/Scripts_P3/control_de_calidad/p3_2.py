# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 11:50:57 2022

@author: bolivar

Control de Calidad
Calificación:
Una empresa siderúrgica, tiene como política realizar elaboraciones de
Alambrón según las especificaciones dadas por sus clientes (% en peso de
Carbón y Magnesio), en este sentido han decidido automatizar su proceso de
control de calidad del producto terminado, con el fin de que sea más fácil el
proceso aprobación o no de un lote de alambrón producido.
El ingeniero de calidad ha decidido que un día de producción se almacene,
en el archivo de datos “pruebas.txt”, la información de cada lote de
producción de la siguiente forma:
Nro del Lote, %Peso Mín de C, %Peso Máx de C, %Peso Medido de C, %Peso Mín de Mg, %Peso Máx de Mg y %Peso Medido de Mg

Requerimientos
a) Desarrolle un subprograma que lea la información de una línea del archivo prueba.txt y retorne los datos leídos.
(El número del archivo pasa como parámetro)
b) Desarrolle un subprograma que dados Valor Máx, Valor Medido y Valor Mín, determine si:
(Valor Máx>Valor Medido>Valor Mín). 
c) Desarrolle un subprograma que imprima en un archivo (El número del archivo pasa como parámetro) la
información de un lote de Alambrón producido. 

Programa Principal
Elabore una aplicación VB de consola que haciendo uso del archivo “pruebas.txt”, determine e imprima:
a) Para cada lote, dependiendo si el producto es aceptado (cumple con las especificaciones de porcentaje máximo y
mínimo en peso de Carbón y Magnesio) o no, imprima la información del lote en el archivo de datos
“aceptados.txt” o “rechazados.txt”.
b) Para todos los lotes, imprimir por consola, el porcentaje de lotes rechazados en un día.
         
pruebas.txt
16531, 5.00, 8.00, 9.60, 30.00, 32.00, 28.50
19405, 4.00, 7.00, 5.60, 20.00, 23.00, 20.90
19765, 4.00, 6.00, 3.20, 32.00, 37.00, 33.60
21505, 1.00, 3.00, 2.40, 25.00, 31.00, 27.55
23213, 3.00, 4.00, 2.40, 23.00, 25.00, 24.80
23347, 1.00, 3.00, 2.40, 29.00, 31.00, 29.45
24188, 4.00, 5.00, 4.90, 21.00, 23.00, 22.00

aceptados.txt
19405 4.00 7.00 5.6 20.0 23.0 20.9
21505 1.00 3.00 2.4 25.0 31.0 27.55
23347 1.00 3.00 2.4 29.0 31.0 29.45
24188 4.00 5.00 4.9 21.0 23.0 22.0

rechazados.txt
16531 5.00 8.00 9.6 30.0 32.0 28.5
19765 4.00 6.00 3.2 32.0 37.0 33.6
23213 3.00 4.00 2.4 23.0 25.0 24.8

Salida por pantalla:
Porcentaje de lotes rechazados: 42.86 %
"""

def LeerLinea(registro):
    # Subprograma que lee la informacion de una linea del archivo
    linea = registro.split(',')
    Nlote = int(linea[0])
    PminC = float(linea[1])
    PmaxC = float(linea[2])
    PmedC = float(linea[3])
    PminMg = float(linea[4])
    PmaxMg = float(linea[5])
    PmedMg = float(linea[6])
    return Nlote, PminC, PmaxC, PmedC, PminMg, PmaxMg, PmedMg

# Subprograma que verifica que el valor medido este en el rango
def cumple( Min: float,  Max: float, Med: float):
    return Med < Max and Med > Min


# Subprograma que Imprime la informacion de una linea a un archivo
def imprimir_linea(arch: int, Nlote: int, PminC: float, PmaxC: float, PmedC: float, PminMg: float, PmaxMg: float, PmedMg: float):
    arch.write(f'{Nlote} {valor(PminC)} {valor(PmaxC)} {valor(PmedC)} {valor(PminMg)} {valor(PmaxMg)} {valor(PmedMg)}\n')
    
# Subprogramas adicionales
# Subprograma que genera como cadena el texto la impresion de un dato
def valor( X: float):
    return "%.2f" % X


def main():
    # Que tengo?
    Nlote: int
    PminC: float
    PmaxC: float
    PmedC: float
    PminMg: float
    PmaxMg: float
    PmedMg: float

    # Que quiero?
    PorcRec: float

    # Variables auxiliares
    Crech: int = 0
    Clotes: int = 0

    # Manejo de archivos
    arch1 = open("pruebas.txt", 'r')
    arch2 = open("aceptados.txt", 'w')
    arch3 = open("rechazados.txt", 'w')

    # Ciclo de lectura
    for registro in arch1:
        Nlote, PminC, PmaxC, PmedC, PminMg, PmaxMg, PmedMg = LeerLinea(registro)

        # Verificacion del lote
        if cumple(PminC, PmaxC, PmedC) and cumple(PminMg, PmaxMg, PmedMg):
            imprimir_linea(arch2, Nlote, PminC, PmaxC, PmedC, PminMg, PmaxMg, PmedMg)
        else:
            imprimir_linea(arch3, Nlote, PminC, PmaxC, PmedC, PminMg, PmaxMg, PmedMg)
            Crech += 1

        # Determinacion del numero de lotes procesados en el dia
        Clotes += 1
    

    # Calculo e impresion del porcentaje de lotes rechazados
    PorcRec = Crech * 100 / Clotes
    print("Porcentaje de lotes rechazados: %.2f %%" % PorcRec)
    
    # Cierre de archivos
    arch1.close()
    arch2.close()
    arch3.close()
    
    # Mensaje al usuario
    input("Pulse una tecla para finalizar")

if __name__ == "__main__":
    main()

