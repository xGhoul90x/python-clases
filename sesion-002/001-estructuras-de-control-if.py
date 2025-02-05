"""
Estructura de control (de flujo) condicional
Sintaxis:

# Forma 1:
if(condicion):
    sentencia 1
    sentencia 2
    sentencia 3

# Forma 2
if(condicion):
    sentencia 1
    sentencia 2
    sentencia 3
else:
    sentencia 4
    sentencia 5
    sentencia 6

# Forma 3
if(condicion 1):
    sentencia 1
else if(condicion 2):
    sentencia 2
else if(condicion 3):
    sentencia 3
else:
    sentencia 4

# Condicion: Puede ser simple o compleja
"""
saldo = 100
edad = 17
costo_entrada = 500
if(saldo >= costo_entrada and edad >= 18):
    print("Sí procederá la compra")
else:
    print("No procederá la compra")


