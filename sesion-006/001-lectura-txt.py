f = open("dato.txt", "r") # with open("dato.txt", "r") as fichero:
lineas = f.readlines()
print(lineas)
num = 0
for linea in lineas:
    print("linea #", num, "->", linea, end="")
    num += 1

