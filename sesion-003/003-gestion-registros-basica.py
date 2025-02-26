"""
Crear un sistema de gestion de registros de pacientes
Debemos almacenar nombres, edades, estaturas, estado civil: s, c, v, d, esta_vivo
"""
# Lista vacía
registros_lista = [] # list()

# Lectura de datos
nombre = input("Nombre: ")
edad = int(input("Edad: "))
estatura = float(input("Estatura: "))
estado_civil = input("Estado civil (s: soltero, c: casado, v: viudo, d: divorciado): ")
esta_vivo = bool(input("Esta vivo (1: si, 0: no): "))
# Creando la variable
registro = {"nombre": nombre, "edad": edad, "estatura": estatura, "estado_civil": estado_civil, "esta_vivo": esta_vivo}
# Agrwgando el valro de la variable a la lista
registros_lista.append(registro)

nombre = input("Nombre: ")
edad = int(input("Edad: "))
estatura = float(input("Estatura: "))
estado_civil = input("Estado civil (s: soltero, c: casado, v: viudo, d: divorciado): ")
esta_vivo = bool(input("Esta vivo (1: si, 0: no): "))
registro = {"nombre": nombre, "edad": edad, "estatura": estatura, "estado_civil": estado_civil, "esta_vivo": esta_vivo}
registros_lista.append(registro)

print(registros_lista)
