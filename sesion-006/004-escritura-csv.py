# Escritura desde una lista de listas
cabecera = ["nombre", "edad", "peso"]
datos = [["José Luis", 28, 55],
         ["Ana María", 32, 60],
         ["Pedro", 25, 80]
         ]
archivo = open("salida.csv", "w", encoding="utf-8")
archivo.write(",".join(map(str, cabecera)) + "\n")
for elemento in datos:
    archivo.write(",".join(map(str, elemento)) + "\n")

# Escritura desde una lista de diccionarios
cabecera2 = ["nombre", "dni", "peso", "estatura"]
datos2 = [{'nombre': 'José Luis', 'dni': '00000011', 'peso': '80', 'estatura': '1.69'},
          {'nombre': 'María Luisa', 'dni': '00000012', 'peso': '75', 'estatura': '1.58'},
          {'nombre': 'Ricardo', 'dni': '00000013', 'peso': '61', 'estatura': '1.73'}]

archivo2 = open("salida2.csv", "w", encoding="utf-8")
archivo2.write(",".join(map(str, cabecera2)) + "\n")
for elemento in datos2:
    archivo2.write(elemento["nombre"]+",")
    archivo2.write(elemento["dni"]+",")
    archivo2.write(elemento["peso"]+",")
    archivo2.write(elemento["estatura"]+"\n")

