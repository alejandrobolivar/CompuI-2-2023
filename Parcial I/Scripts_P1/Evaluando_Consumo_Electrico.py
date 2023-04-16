'''El 09 de febrero de 2010 fue decretada oficialmente la emergencia eléctrica en Venezuela, lo cual confirmó la crisis
eléctrica que se estaba viviendo en el país. Debido a esto las comunidades están evaluando su consumo eléctrico; para
ello se tiene la información de las lecturas de los medidores, de los suscriptores de una zona aleatoriamente
seleccionada, la información es la siguiente:

Número de Contrato, Tipo de Suscriptor, Lectura inicial y final del medidor en KWh

Desarrolle un programa en VB2010, que procese la información antes mencionada
y determine e imprima:

a) Consumo eléctrico de cada suscriptor (2 ptos)
b) Monto de la factura en Bs por cada suscriptor (3 ptos)
c) Monto total en Bs. que deben pagar los suscriptores residenciales de alto
consumo por concepto de multa (2 ptos)
d) Consumo eléctrico total de la zona en estudio (2 ptos)
e) Promedio de consumo eléctrico de los suscriptores de tipo residencial
considerados de alto consumo (2 ptos)
f) Número de Contrato del primer suscriptor de tipo residencial procesado
considerado de alto consumo (2 ptos)
Consideraciones:
 El tipo de suscriptor se tomará como 1 para Residencial y 2 para Comercial
 El consumo eléctrico se determina como la diferencia entre las lecturas del medidor.
 Se consideran usuarios de alto consumo residencial aquellos cuyo consumo sea superior a 500 KWh.
 Cada KWh residencial cuesta Bs. X y cada KWh comercial cuesta Bs. Y.
 La multa por ser usuario residencial de alto consumo es de 50% del monto a pagar por el consumo.
 El monto de la factura será la suma del monto a pagar por el consumo eléctrico más la multa, en caso de ser usuario
residencial de alto consumo'''

# INICIALIZACION DE VARIABLES
acum_ce = 0
acum_ce_alco = 0
cont_ce_alco = 0
band = 0
resp = 1
tarifa_res = float(input('Ingrese el monto en Bs a pagar por los suscriptores residenciales: '))
tarifa_com = float(input('Ingrese el monto en Bs a pagar por los suscriptores comerciales: '))
while resp == 1:
    contrato = int(input('Ingrese el numero de contrato: '))
    linicial = float(input('Ingrese la lectura inicial del medidor: '))
    lfinal = float(input('Ingrese la lectura final del medidor: '))
    ts = int(input('Ingrese el tipo de suscriptor: \nResidencial (1) \nComercial (2) \n'))
# RESPUESTA a
    ce = lfinal - linicial
# RESPUESTA d
    acum_ce += ce
# RESPUESTA b
    if ts == 1:
        monto = ce * tarifa_res
    elif ts == 2:
        monto = ce * tarifa_com
    print('Su consumo eléctrico es: ', ce)
# RESPUESTA c
    if ts == 1 and ce > 500:
        multa = monto / 2
        monto = monto + multa
# RESPUESTA e
        acum_ce_alco += ce
        cont_ce_alco += 1
        print('Es un suscriptor de alto cosumo su multa es: {multa:6.2f},y su total a pagar {monto:6.2f}')
    else:
        print(f'Su monto a pagar es: {monto:6.2f}')
# Respuesta f
    if ts == 1 and ce > 500 and band == 0:
        alco_1 = contrato
        band = 1
    resp = int(input('Hay mas suscriptores? \nSI: 1 \nNO: 2'))

ce_zona = acum_ce
if cont_ce_alco == 0:
    print('')
else:
    prom = acum_ce_alco / cont_ce_alco
print(f'El consumo total de la zona de estudio es: {ce_zona}')
print(f'El promedio de consumo electrico de los suscriptores de alto consumo es: {prom:6.2f}')
print(f'El numero de contrato del primer consumidor de alto consumo es: {alco_1}')