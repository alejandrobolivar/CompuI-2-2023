'''
Tiempo de retardo en los vuelos
OBJETIVO: Desarrollar un programa, cuya solución implemente subprogramas tipo procedimiento y funciones.
Problema
Para la administración y mejora del funcionamiento de un Aereopuerto
Nacional, se registra a cada vuelo que parte en un día de trabajo, el número
del vuelo, la hora de salida programada del vuelo y además la hora real en que
se hace efectivo el despege del mismo (Los tiempos estan expresados en hora
militar). De esta manera, es posible calcular el tiempo de demora que un
vuelo tuvo expresado en minutos totales, como la diferencia entre la hora de
salida real y la programada siempre y cuando este resulte un valor positivo.
Nota:
 Si el avión logra salir antes de la hora programada, el tiempo de demora es cero o negativo.
 Considere que todos los vuelos se realizan durante el mismo día.
 Además, recuerde que: 1 Hora = 60 Minutos

PROBLEMA
En un archivo de datos de nombre vuelos.txt se almaceno en cada línea la siguiente informacion de un vuelo realizado
en el día, el número de vuelo, la hora de salida programa (expresada en formato militar; hh:mm) y la hora de salida real
(expresada en formato militar; hh:mm). Desarrolle un programa bajo consola, que utilizando el archivo
Vuelos.Txt, determine e imprima hacia el archivo de datos resultados.txt el número de vuelo, la salida programada
de salida y el tiempo de demora (expresado en hh: mm), y por pantalla reporte la información de ¿cúal fue el vuelo con
la mayor demora?
REQUERIMIENTOS
Para la solución del problema debe definir y utilizar:
1. Un subprograma que lea desde un archivo de datos, una línea que contenga la informacion del número de vuelo de
un avión, la hora pautada de salida y la hora en que realmente salio.
2. Un subprograma que convierta un tiempo expresado en horas y minutos en su tiempo total expresado en minutos.
3. Un subprograma que dado dos tiempos expresados en horas y minutos, devuelva, ¿cuántos minutos han
transcurridos entre ambos?
4. Un subprograma que imprima hacia un archivo de datos (sin salto de línea), un tiempo expresado en horas y minutos
de la siguiente manera, las horas y los minutos representado en dos digitos y separdos por dos puntos (:) , en caso de
ser el valor inferior a 10, imprima un cero por delante
Ejemplo de los archivos:

Por ejemplo:
vuelos.txt
201 6 15 7 20
205 7 00 6 50
301 8 00 8 00
302 9 15 10 40
305 16 20 16 35

resultados.txt
VUELO HORA_SALIDA DEMORA(hh:mm)
201 06:15 01:05
205 07:00 a tiempo
301 08:00 a tiempo
302 09:15 01:25
305 16:20 00:15   

Salida por pantalla:
El vuelo con mayor demora fue el 302 con salida programada a las 09:15 con 85 minutos de demora
'''
def leer(registro):
	linea = registro.split(',')
	vuelo = int(linea[0])
	hp = int(linea[1])
	mp = int(linea[2])
	hs = int(linea[3])
	ms = int(linea[4])
	return vuelo, hp, mp, hs, ms
	
def tiempom(h, m):
	return h*60 + m
	
def deltat(h1, m1, h2, m2):
	return tiempom(h2,m2) - tiempom(h1,m1)

def imprimir(arch, h, m):
	arch.write('%02d:%02d\t'%(h,m))
	
def main():
    #datos del vuelo
    numeros: int
    hi: int
    mi: int
    hf: int
    mf: int
    #mayor retrasados
    mtiempo: int
    mid: int
    mh: int
    mm: int
    mtiempo: int = 0
    #Apertura de Archivos
    arch1 = open('vuelos.txt','r')
    arch2 = open('resultante.txt','w')
    for registro in arch1:
    	numeros,hi,mi,hf,mf = leer(registro)
    	arch2.write(str(numeros) + '\n')
    	imprimir(arch2,hi,mi)
    	retraso = deltat(hi,mi,hf,mf)
    	if retraso > mtiempo:
    	   	mtiempo = retraso
    	   	mid = numeros
    	   	mh = hi
    	   	mm = mi
    	if retraso <= 0:
    	  arch2.write('A tiempo')
    	else:
    	   	h = retraso//60
    	   	m = retraso%60
    	   	imprimir(arch2,h,m)
    	   	arch2.write('\n')
    print('El vuelo con mayor demora fue el ',mid,'con salida programada a las ',mh, ':',mm,' con ', mtiempo, ' minutos de demora')
    arch1.close()
    arch2.close()
if __name__=="__main__":
		main()