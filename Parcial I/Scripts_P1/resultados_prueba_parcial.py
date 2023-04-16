'''
ESCENARIO: RESULTADOS PRUEBA PARCIAL
El departamento de computación lo contrata a usted para que desarrolle un programa que de los resultados 
del primer parcial de un grupo de alumnos, a la cual se le suministra la siguiente información:
    Nombre del alumno, Hora y minutos de llegada a la prueba.
Si logra entrar a la prueba:
    Hora y minutos de salida y calificación obtenida en la prueba.
Procese la información anterior y determine e imprima por consola:
Para cada alumno:
1.	Si pudo entrar o no a la prueba indicándolo con un mensaje,
    en caso de entrar en cuanto tiempo desarrollo la prueba en horas y minutos.
2.	Si llego temprano a la prueba indíquelo con un mensaje y cuánto tiempo espero para entrar a la misma en minutos.
Para todos los alumnos:
3.	Porcentaje de alumnos que llegaron temprano con respecto al total que entraron a la prueba.
4.	Nombre del alumno que obtuvo la mayor calificación en la prueba habiendo desarrollado la misma en el menor tiempo,
    en caso de haber más de un alumno en las mismas condiciones, reporte el primero y el último.
5.	Cuantos estudiantes se procesaron antes de encontrar el primer estudiante que no entro a la prueba.
6.	Promedio de las notas de los alumnos que llegaron después de transcurridos 45 minutos de haber comenzado la prueba.
Consideraciones:
•	Una hora tiene 60 minutos.
•	La prueba comienza a las 8:00 AM (480 minutos de día) y termina a las 10:00 AM (600 minutos de día)
•	Todo alumno que llegue a la 9:01 AM (541 minutos del día) o después no entra a la prueba.
'''

# inicializacion de variables:
cont = 0
band = True
cont_entraron = 0
cont_temprano = 0
cont_noentro = 0
mayor_calif = 0
menor_tiempo = 1000
primero_mayor_calif = ''
ultimo_mayor_calif = ''
cont_45 = 0
acum_45 = 0
# variable para la condicion while
resp = "s"
while resp.lower() == 's' :
    nombre = input('Nombre del alumno: ')
    entrada_hora = int(input('Hora de entrada: '))
    entrada_min = float(input('Minutos de entrada: '))
    entrada_tot_min = entrada_hora * 60 + entrada_min
    cont += 1
    if entrada_tot_min < 541:  # p1 Entro a la prueba
        cont_entraron += 1
        salida_hora = int(input('Hora de salida: '))
        salida_min = int(input('Minutos de salida: '))
        calificacion = int(input('Calificación: '))
        salida_tot_min = salida_hora * 60 + salida_min
        print('Si puede ingresar a la prueba')  # p1
        duracion = salida_tot_min - entrada_tot_min
        if entrada_tot_min > 525 :  # p6
            acum_45 += calificacion
            cont_45 += 1
        if entrada_tot_min < 480:  # p2 LLego temprano
            cont_temprano += 1  # p3
            espera = 480 - entrada_tot_min
            print(f'Ha llegado temprano a la prueba y tuvo que esperar {espera} minutos')  # p2
            duracion -= espera  # como llego temprano le resto ese tiempo a la duración
        duracion_hora = int(duracion // 60)
        duracion_min = int(duracion % 60)
        print(f'Duración en la prueba = {duracion_hora}:{duracion_min}')  # p1
        if duracion < menor_tiempo:  # p4
            menor_tiempo = duracion
            if calificacion > mayor_calif:
                mayor_calif = calificacion
                primero_mayor_calif = nombre
                ultimo_mayor_calif = nombre
            if calificacion == mayor_calif:
                ultimo_mayor_calif = nombre
    else:  # p1 No entro a la prueba
        cont_noentro += 1
        print('Ha llegado tarde a la prueba y no puede ingresar')  # p1
        if band:  # p5
            procesados = cont
    resp = input('Desea añadir más estudiantes? Si(S) no(N):' )
if cont_entraron != 0:  # p3
    porc = cont_temprano * 100 / cont_entraron
    print('Porcentaje de alumnos que llegaron temprano con respecto al total que entraron a la prueba= %.2f' % porc)
if primero_mayor_calif != '':  # p4
    print('Primer alumno que obtuvo la mayor calificación en la prueba habiendo desarrollado la misma en el menor tiempo= {primero_mayor_calif}')
if ultimo_mayor_calif != '':  # p4
    print('Último alumno que obtuvo la mayor calificación en la prueba habiendo desarrollado la misma en el menor tiempo= {ultimo_mayor_calif}')
print('La cantidad de estudiantes procesados antes de encontrar al primero que NO entró es de: {procesados}')  # p5
if cont_45 != 0:  # p6
    prom = ( acum_45 / cont_45 )
    print('Promedio de notas en alumnos que llegaron después de transcurridos los 45 min es de: %.2f' % prom)