"""
Crear un sistema de gestion de registros de pacientes
Debemos almacenar nombres, edades, estaturas, estado civil: s, c, v, d, esta_vivo
"""
# Lista vacía
registros_lista = [] # list()
opcion = "s"
posicion = 1
while(opcion == "s"):
    print("Datos del usuario #", posicion)
    # Lectura de datos
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    estatura = float(input("Estatura: "))
    estado_civil = input("Estado civil (s: soltero, c: casado, v: viudo, d: divorciado): ")
    esta_vivo = bool(input("Esta vivo (1: si, 0: no): "))
    
    # Creando la variable de tipo diccionario
    registro = {"nombre": nombre, "edad": edad, "estatura": estatura, "estado_civil": estado_civil, "esta_vivo": esta_vivo}

    # Agrwgando el valro de la variable a la lista
    registros_lista.append(registro)

    posicion += 1 # posicion = posicion + 1

    opcion = input("¿Deseas seguir ingresando datos? (s: si, n: no): ")
    while(not(opcion == "s" or opcion == "n")):
        print("Error! Opción incorrecta")
        opcion = input("¿Deseas seguir ingresando datos? (s: si, n: no): ")

print(registros_lista)
