'''
Variable medida Rango
Leucocitos 4,5 – 11,0 mm3
Hematocrito 42 – 52 ml/dl
Plaquetas 150 – 400 mm3
Hemoglobina (mujer) 12 – 15 g/dl
Hemoglobina (hombre) 13 – 17 g/dl
Linfocitos 20 – 40 %

PROBLEMA
En un laboratorio clínico se suministra diariamente en una base de datos la información de los pacientes
que se van a realizar en el día una hematología completa, los datos que se pueden encontrar son:

Nombre del paciente, genero (m=masculino f=femenino), leucocito, hematocrito, plaquetas.
Hemoglobina y linfocitos

Se desea que usted desarrolle un algoritmo que procese la información de los pacientes y suministre los
siguientes resultados:

Por cada paciente:
Indicar si cada valor medido para la hemoglobina durante el análisis de laboratorio esta o no fuera
de rango, con las palabras ALTO, BAJO o NORMAL. Por ejemplo Leucocito=3.1 mm3 → BAJO

Para todos los pacientes:
1) Porcentaje de mujeres anémicas
2) Cantidad de pacientes con valor de plaquetas por encima de 400 mm3
3) Promedio de linfocitos en el día
4) Paciente con el menor valor de hematocrito, debe reportar el primero e indicar cuantos
además de él tienen ese valor en su hematología.
5) Primer hombre en tener su leucocito menor a 4 mm3

'Variables de Entrada
nombre
genero, resp
leuc, hemat, plaq, hemog, linf

'Variables de Proceso
cont_muj_anem, cont_muj, cont_pac
cont_hemat, cont_leuc
band_min_hemat
band_menor4
acum_linf

'Variables de Salida
porc_muj_anem
cant_pac_plaq_may400
prom_linf_dia, min_hemt
pac_men_val_hemat  = ""
prim_pac_men_hemat  = ""
prim_hom_leuc_menor4  = ""

'''

cont_pac = 0
acum_linf = 0

# Proceso
while  resp.upper() =='S':
    # Datos de Entrada
    nombre = input("Indique el Nombre del Paciente: ")
    genero = input("Indique el Genero m=masculino f=femenino :")
    leuc = input("Indique el valor de Leucocito: ")
    hemat = input("Indique el valor de Hematocrito: ")
    plaq = input("Indique el valor de Plaquetas: ")
    hemog = input("Indique el valor de Hemoglobina: ")
    linf = input("Indique el valor de Linfocitos: ")

    # Pregunta 3
    cont_pac += 1
    acum_linf += linf
    cont_muj_anem = 0
    cont_muj = 0
    cant_pac_plaq_may400 = 0

    if genero == "m":  # Masculino
        if hemog >= 13 and hemog <= 17:
            print("El rango de Hemoglobina es Normal")
        elif hemog < 13:
            print("El rango de Hemoglobina es Bajo")
        else:
            print("El rango de Hemoglobina es Alto")

        if band_menor4 == 0 and leuc < 4:  # Pregunta 5
            prim_hom_leuc_menor4 = nombre
            band_menor4 = 1

    else:  # Femenino
        if hemog >= 12 and hemog <= 15:
            print("El rango de Hemoglobina es Normal")
        elif hemog < 12:
            print("El rango de Hemoglobina es Bajo")
            cont_muj_anem += 1  # Pregunta 1
        else:
            print("El rango de Hemoglobina es Alto")

        cont_muj += 1  # Pregunta 1

    if plaq > 400:  # Pregunta 2
        print("Paciente con plaquetas alta")
        cant_pac_plaq_may400 += 1

    if band_min_hemat == 0:  # Pregunta 4. Primer Paciente con el menor valor de hematocrito
        band_min_hemat = 1
        min_hemt = hemat
        prim_pac_men_hemat = nombre
        cont_hemat = 1
    elif hemat < min_hemt:  # Reemplaza el Primer Paciente con el menor valor de hematocrito
        min_hemt = hemat
        prim_pac_men_hemat = nombre
        cont_hemat = 1
    elif hemat == min_hemt:  # Tiene el mismo menor valor de hematocrito
        cont_hemat += 1

    resp = input("¿Otro paciente [S/N]:? ")

#   Salida de Datos
if cont_muj != 0:
    porc_muj_anem = cont_muj_anem / cont_muj * 100
    print("1) El porcentaje de mujeres anémica es de :" , porc_muj_anem , "%")
else:
    print("No hubo pacientes femeninas")

if cant_pac_plaq_may400 == 0:  # Pregunta 2
    print("No hubo pacientes con plaquetas elevadas")
else:
    print("2)El total de pacientes con plaquetas elevada a los 400 mm^3 es de: " , cant_pac_plaq_may400)

if cont_pac != 0:  # Pregunta 3
    prom_linf_dia = acum_linf / cont_pac
    print("3) El promedio de linfocitos al dia es de: " , prom_linf_dia)
else:
    print("Sin pacientes")

if cont_hemat != 0:  # Pregunta 4
    print("4) El primer paciente con el menor valor de Hematocrito es: " , prim_pac_men_hemat)
    if cont_hemat > 0:
        print("Y hubo " , cont_hemat , " pacientes con esa misma cantidad de Hematocritos")

# Pregunta 5
if band_menor4 == 1:
    print("5) El primer hombre en tener su leucosito menor a 4 mm^3 es:" , prim_hom_leuc_menor4)
else:
    print("No hay hombre con leucosito menor a 4 mm^3")