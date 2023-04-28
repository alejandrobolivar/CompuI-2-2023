'''
Los estudiantes de la Facultad de Ciencias de la Salud inician una jornada de
despistaje de hipertensión arterial, registrando durante días consecutivos la
presión de un conjunto de personas. Para el procesamiento de la información
le solicitarán apoyo a la Facultad de Ingeniería a la cual le hacen entrega del
archivo de datos “Tensiones.txt” con la siguiente estructura:
Para cada persona se registra:
NOMBRE, GÉNERO, EDAD Y CANTIDAD DE MEDICIONES
Y para cada una de las mediciones de la persona:
FECHA (DÍA/MES), PRESIÓN SISTÓLICA y PRESIÓN DIASTÓLICA expresadas en MMHG (milímetros de mercurio).
Se le pide a ud. que desarrolle una aplicación de consola VB2010 que procese el archivo “Tensiones.txt” y
genere el archivo de dato “resultados.txt” el cual debe contener por cada paciente NOMBRE, EDAD y un
mensaje que indique si está sano o es hipertenso, adicionalmente se requiere que determine y muestre las
siguientes estadísticas en pantalla:
Por cada Paciente:
1. Porcentaje de mediciones consideradas como Tensión Alta. (1.5 ptos)
2. Fecha, presión sistólica y diastólica en donde el paciente registro menor diferencia entre las dos
presiones. (1.5 ptos)
Para todos los Pacientes:
3. Nombre y Edad del primer paciente con todas las mediciones de tensión normal. (1.5 ptos)
4. Género (Masculino o Femenino) que tiene más pacientes hipertensos. (1.5 ptos)
CONSIDERACIONES
1. Se considera una Tensión Alta: si la Presión Sistólica está por encima de 139 mmHg o la Presión
Diastólica está por encima de 89 mmHg.
2. Un paciente es hipertenso si al menos la mitad de las mediciones registradas se consideran como
tensión alta.


'''


        'Entradas
        Dim Nombre As String
        Dim Genero As Char
        Dim Edad, Cant_Mediciones As Integer
        Dim Fecha As String
        Dim PresionS, PresionD As Integer

        'Salidas
        Dim Porc_Tension_Alta As Single
        Dim Fecha_Menor As String
        Dim PresionS_Menor, PresionD_Menor As Integer
        Dim Nomb_Primero As String
        Dim Edad_Primero As Integer
        Dim Gen_Mayor_Cant_Hipertensos As String

        'Procesos
        Dim Cant_Mediciones_Altas As Integer
        Dim Band_Menor As Boolean
        Dim Diferencia, Dif_Menor As Integer
        Dim Band_Primero As Boolean
        Dim Cant_Masculino_Hipertensos, Cant_Femenino_Hipertensos As Integer
        Dim I As Integer

        'Manejo de Archivos
        FileOpen(1, "tensiones.txt", OpenMode.Input)
        FileOpen(2, "resultados.txt", OpenMode.Output)

        'Inicializaciones (TODOS LOS PACIENTES)
        Band_Primero = True
        Cant_Masculino_Hipertensos = 0
        Cant_Femenino_Hipertensos = 0

        'Ciclo Externo (CADA PACIENTE)
        While Not EOF(1)

            'Lectura de datos de cada paciente
            Input(1, Nombre)
            Input(1, Genero)
            Input(1, Edad)
            Input(1, Cant_Mediciones)

            'Inicializaciones (CADA PACIENTE)
            Cant_Mediciones_Altas = 0
            Band_Menor = True

            'Ciclo Interno (CADA MEDICIÓN)
            For I = 1 To Cant_Mediciones

                'Lectura de datos de cada medición
                Input(1, Fecha)
                Input(1, PresionS)
                Input(1, PresionD)

                'Determinar si una medición es considerada como tensión alta
                If (PresionS > 139) Or (PresionD > 89) Then
                    Cant_Mediciones_Altas = Cant_Mediciones_Altas + 1
                End If

                'Cálculo de la menor dif. entre presiones
                Diferencia = Math.Abs(PresionS - PresionD)

                If Band_Menor Then
                    Fecha_Menor = Fecha
                    PresionS_Menor = PresionS
                    PresionD_Menor = PresionD
                    Dif_Menor = Diferencia
                    Band_Menor = False
                ElseIf Diferencia < Dif_Menor Then
                    Fecha_Menor = Fecha
                    PresionS_Menor = PresionS
                    PresionD_Menor = PresionD
                    Dif_Menor = Diferencia
                End If

            Next

            'Imprimir datos en el archivo
            If (2 * Cant_Mediciones_Altas) >= Cant_Mediciones Then 'Paciente Hipertenso
                PrintLine(2, Nombre, Edad, "Hipertenso")

                'Cálculo del género con más pacientes hipertensos
                If (Genero = "F") Or (Genero = "f") Then
                    Cant_Femenino_Hipertensos = Cant_Femenino_Hipertensos + 1
                ElseIf (Genero = "M") Or (Genero = "m") Then
                    Cant_Masculino_Hipertensos = Cant_Masculino_Hipertensos + 1
                End If

            Else 'Paciente sano
                PrintLine(2, Nombre, Edad, "Sano")
            End If

            'Cálculo e impresión del porcentaje de mediciones consideradas como tensión alta
            Porc_Tension_Alta = (Cant_Mediciones_Altas / Cant_Mediciones) * 100

            Console.WriteLine("Paciente:{0}, Porc. Med. Altas: {1}%", Nombre, Porc_Tension_Alta)

            'Primer paciente con todas las med. consideradas tensión normal
            If Cant_Mediciones_Altas = 0 Then
                If Band_Primero Then
                    Nomb_Primero = Nombre
                    Edad_Primero = Edad
                    Band_Primero = False
                End If
            End If

            'Imprimir datos del registro con menor diferencia entre las 2 presiones
            Console.WriteLine("Nombre del Paciente: " & Nombre)
            Console.WriteLine("Registro con menor dif: Fecha:{0}, PS:{1}, PD:{2}", Fecha_Menor, PresionS_Menor, PresionD_Menor)

        End While

        'Imprimir Primer paciente con todas las med. consideradas tensión normal
        If Not Band_Primero Then
            Console.WriteLine("Primer paciente con todas las med. de tensión normales: Nombre:{0}, Edad:{1}", Nomb_Primero, Edad_Primero)
        Else
            Console.WriteLine("Ningun paciente con med. de tensión normales")
        End If

        'Imprimir el género con mayor cantidad de pacientes hipertensos
        If Cant_Masculino_Hipertensos > Cant_Femenino_Hipertensos Then
            Gen_Mayor_Cant_Hipertensos = "Masculino"
            Console.WriteLine("El género con mayor cantidad de pacientes hipertensos es: " & Gen_Mayor_Cant_Hipertensos)
        ElseIf Cant_Femenino_Hipertensos > Cant_Masculino_Hipertensos Then
            Gen_Mayor_Cant_Hipertensos = "Femenino"
            Console.WriteLine("El género con mayor cantidad de pacientes hipertensos es: " & Gen_Mayor_Cant_Hipertensos)
        Else
            Console.WriteLine("Ambos géneros tiene igual cantidad de pacientes hipertensos")
        End If

        'Cierre de Archivos
        FileClose(1)
        FileClose(2)



