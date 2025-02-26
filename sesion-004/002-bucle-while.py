"""
Bucle while
- Mientras se cumpla una condicion, se repiten las sentencias contenidas en el bucle
"""
x = 5
while(x>0):
    print(x, end=" ")
    x = x-1
print()

lista = []
opcion = "s"
while(opcion == "s"):
    valor = int(input("Valor: "))
    lista.append(valor)
    opcion = input("Deseas ingresar otro valor (s: sí, n: no): ")
    # Validacion
    while(opcion != "s" and opcion != "n"):
        print("Opción incorrecta")
        opcion = input("Deseas ingresar otro valor (s: sí, n: no): ")

print("Lista:", lista)