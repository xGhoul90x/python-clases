"""
Crea un archivo python tal que lea desde un fichero los datos de personas
nombre,anho_nac,estatura_cm
Y cree otro archivo que guarde lo siguiente
nombre,edad,estatura_m
"""
fichero = open("datos_personas.csv", "r", encoding="utf-8")
cabecera = fichero.readline() # Leo la cabecera para despues solo tener las lineas de los datos
cabecera = cabecera.strip()
cabecera = cabecera.split(",")
# print(cabecera)
lineas = fichero.readlines()
personas = [] # Voy a guardar una lista con los datos de los personas
for linea in lineas:
    linea = linea.strip() # Elimina espacios a los extremos y saltos de línea al final
    linea = linea.split(",") # Divido el contenido de la linea por las comas, y todo se ingresa a una lista
    persona = {} # Diccionario para guardar datos del persona correspondiente a la linea actual
    for pos in range(len(cabecera)):
        persona[cabecera[pos]] = linea[pos]
    personas.append(persona)

# Transformacion: crear valores a partir de otros y procesarlos
for pos in range(len(personas)):
    personas[pos]["edad"] = 2025-int(personas[pos]["anho_nac"])
    personas[pos]["estatura_m"] = int(personas[pos]["estatura_cm"])/100
    print(personas[pos])

# Escriuta de datos
cabecera2 = ["nombre", "edad", "estatura_m"]

archivo2 = open("datos_personales_transformados.csv", "w", encoding="utf-8")
archivo2.write(",".join(map(str, cabecera2)) + "\n")
for elemento in personas: # Personas es la lista de diccionarios que contiene los datos
    archivo2.write(elemento["nombre"]+",")
    archivo2.write(str(elemento["edad"])+",")
    archivo2.write(str(elemento["estatura_m"])+"\n")