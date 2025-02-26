"""
Crear 3 listas en las que estan los datos de dnis, nombres, edades
El primer elemento de la lista dni, corresponde al primero de la lista nombres y la lista edades
Leer un dni, si existe, darle la bienvenida saludando por su nombre
E imprimir la edad de la persona
"""
dnis_lista = ["00000011", "00000012", "00000013", "00000014"]
nombres_lista = ["Jose Luis", "Ana Maria", "Pedro Jose", "Maria Luisa"]
edades_lista = [21, 29, 30 , 35]
dni_ingresado = input("DNI a consultar: ")
pos_encontrado = -1 # Asumo por defecto una posición inválida

longitud = len(dni_ingresado)

for pos in range(longitud):
    if(dnis_lista[pos] == dni_ingresado):
        pos_encontrado = pos
        break

if pos_encontrado != -1:
    print("Hola", nombres_lista[pos_encontrado])
    print("Edad:", edades_lista[pos_encontrado])
else:
    print("DNI inválido")

"""
# For aNO optimizada: Hace doble búsqueda
if dni_ingresado in dnis_lista:
    pos_encontrado = None
    for pos in range(4):
        if dnis_lista[pos] == dni_ingresado:
            pos_encontrado = pos
    print("Hola", nombres_lista[pos_encontrado])
    print("Edad:", edades_lista[pos_encontrado])
else:
    print("DNI inválido")
"""