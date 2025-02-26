""""
Funciones
- Inician con la palabra reservada def
- Se coloca un nombre, que sigue el standard de nombres de variables
- Puede tener 0, 1... n argumentos (parámetros)
- Puede retornar valor(es) (en caso no retorne no se coloca nada)
"""
def saludar():
    print("Hola")

saludar()

def saludar_con_nombre(nombre):
    print("Hola", nombre)

saludar_con_nombre("José")

def saludar_calcular_edad(nombre, anho_nacimientos):
    saludar_con_nombre(nombre)
    edad = 2025-anho_nacimientos
    return edad

def calcular_datos(estatura, peso, anho_nacimiento):
    imc = peso/estatura
    edad = 2025-anho_nacimiento
    return imc, edad

nombre1 = "Pedro"
anho1 = 1998
estatura1 = 1.73
peso1 = 75
edad1 = saludar_calcular_edad(nombre1, anho1)
print("Tu edad es", edad1)

imc1, edad1 = calcular_datos(estatura1, peso1, anho1)
print("edad:", edad1, "imc:", imc1)