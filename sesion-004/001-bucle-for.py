"""
Bucle for
- Se utiliza para iterar sobre datos cuya dimensión es conocida
- Generalmente se apoya en range(n) -> 0,1,2,...,n-1
"""
for i in range(5):
    print(i, end=" ")
print()

for i in range(4, 7): # Imprime desde el 4 hasta antes del 7
    print(i, end=" ")
print()

lista = []
n = int(input("Cantidad de numeros a ingresar: "))
for i in range(n):
    print("Ingreso de datos #", i+1)
    valor = int(input("Valor: "))
    lista.append(valor)
print("Lista:", lista)
