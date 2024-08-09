recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

#asignamos recordatorios antiguos a nuevo apra tener un respaldo y guardar la nueva version de recordatorios
nuevo_recordatorio = recordatorios

#1. Agregamos nuevo evento al recordatorio en un ligar en especifico
nuevo_recordatorio.insert(1, ['2021-02-02', "06:00", "Empezar el Año"])

#2. Editamos un evento en concreto
nuevo_recordatorio[3] = ['2021-07-16', "13:00", "No hacer nada es feriado"]

#3. Eliminar un evento en especifico
del nuevo_recordatorio[2]

#4. Agregar Cena de Navidad en un lugar en especifico y Año nuevo al final donde corresponde
nuevo_recordatorio.insert(4,['2021-12-24', "22:00", "Cena de Navidad"])
nuevo_recordatorio.append(['2021-12-31', "22:00", "Cena de Año Nuevo"])

#Nuevo Output
print("Nuevo Listado de Recordatorios")
print(nuevo_recordatorio)