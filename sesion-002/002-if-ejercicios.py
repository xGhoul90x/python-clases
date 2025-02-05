# Calcular bonos para trabajadores según años de antiguedad (2-5: 100, 6-10:500, 11-15:1000, 16-inf:2000)
antiguedad = int(input("Ingresa la antiguedad del trabajador: "))
print("Valor ingresado:", antiguedad)
bono = 0 # None es valor vacio NaN, NA, ..., 
if(2 <= antiguedad and antiguedad <= 5):
    bono = 100
elif(6 <= antiguedad and antiguedad <= 10):
    bono = 500
elif(11 <= antiguedad and antiguedad <= 15):
    bono = 1000
elif(16 <= antiguedad):
    bono = 2000
print("Bono:", bono)
