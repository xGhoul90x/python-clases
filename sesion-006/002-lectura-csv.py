fichero = open("pacientes.csv", "r", encoding="utf-8")
cabecera = fichero.readline() # Leo la cabecera para despues solo tener las lineas de los datos
cabecera = cabecera.strip()
cabecera = cabecera.split(",")
# print(cabecera)
lineas = fichero.readlines()
pacientes = [] # Voy a guardar una lista con los datos de los pacientes
for linea in lineas:
    linea = linea.strip() # Elimina espacios a los extremos y saltos de línea al final
    linea = linea.split(",") # Divido el contenido de la linea por las comas, y todo se ingresa a una lista
    paciente = {} # Diccionario para guardar datos del paciente correspondiente a la linea actual
    for pos in range(len(cabecera)):
        paciente[cabecera[pos]] = linea[pos]
    pacientes.append(paciente)
    print(paciente)
print(pacientes)