"""
Identifica una parte de la lógica implementada en excel y pásala a python
usando condicionales, listas para validad si está o no en ella, ingreso de datos por consola
"""
dni = input("Ingrese DNI: ")
if(dni in ["46362441", "03266984", "44665145", "43456599"]):
    print("Bienvenido")
    salario = float(input("Ingreso su salario: "))
    horasextras = float(input("Ingrese horas extras generadas: "))
    
    if(horasextras == 0):
        print("Horas extras: No genero")
    elif(1 <= horasextras and horasextras <= 2):
        print("Horas extras: genero S/", end="")
        print(salario / 30 / 8 * horasextras * 1.25)
    else:
        horasextras1 = 2
        horasextras2 = horasextras - 2
        monto1 = salario / 30 / 8 * horasextras1 * 1.25
        monto2 = salario / 30 / 8 * horasextras2 * 1.35
        montototal = monto1 + monto2
        print("Horas extras:  genero S/", end="")
        print(montototal)
        print()
else:
    print("DNI inválido")
