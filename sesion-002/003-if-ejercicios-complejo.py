"""
Un usuario tiene que registrar su ingreso. Si su DNI es valido podrá ingresar
Y si la hora a la que ingresa es antes de las 8, se registrará como asistencia
Si es pasadas las 8 pero antes de las 10, se registrará tardanza
Si llega después de las 10 será considerada como falta
"""
dni = input("DNI: ")
if(dni in ["98765432", "98765411", "98765433", "98765400"]):
    print("Bienvenido")
    horario = float(input("Hora de ingreso: "))
    if(horario <= 8):
        print("Registro: Asistió")
    elif(8 < horario and horario < 10):
        print("Registro: Tandanza")
    else:
        print("Registro: Falta")
else:
    print("DNI inválido")
