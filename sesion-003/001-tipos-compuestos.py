# Listas
print("LISTAS")
lista_numeros = [10,50,9,5]
print(lista_numeros)
lista_numeros.sort()
print(lista_numeros)
print("Longitud:", len(lista_numeros))
print("Elem. pos 2:", lista_numeros[2])
lista_numeros[2] = 100
print(lista_numeros)
lista_numeros.append(999)
print(lista_numeros)

# Tuplas
print("LISTAS")
tupla_nombres = ("Jose", "Ana", "Mario", "Karla")
print(tupla_nombres)

# Diccionarios
personas_dict = {}
personas_dict["00000011"] = {"Nombre": "Jose Luis", "Edad": 21}
personas_dict["00000012"] = {"Nombre": "Ana Maria", "Edad": 29}
personas_dict["00000013"] = {"Nombre": "Pedro Jose", "Edad": 30}
personas_dict["00000014"] = {"Nombre": "Maria Luisa", "Edad": 35}
print(personas_dict)
print(personas_dict["00000013"]["Nombre"])
print(personas_dict["00000013"]["Edad"])

# Lista de diccionarios (Más utilizada)
alumnos_lista = []
alumno1 = {"DNI": "00000011", "Nombre": "Jose Luis", "Edad": 21}
alumnos_lista.append(alumno1)
alumno2 = {"DNI": "00000012", "Nombre": "Ana Maria", "Edad": 29}
alumnos_lista.append(alumno2)
alumno3 = {"DNI": "00000013", "Nombre": "Pedro Jose", "Edad": 30}
alumnos_lista.append(alumno3)
alumno4 = {"DNI": "00000014", "Nombre": "Maria Luisa", "Edad": 35}
alumnos_lista.append(alumno4)

# Tipo set o conjuntos
conjuntito = {15, 15, 13, 15}
print(conjuntito)