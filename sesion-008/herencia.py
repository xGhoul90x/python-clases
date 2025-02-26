class Vehiculo: # Clase padre
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def descripcion(self):
        return f"Vehículo: {self.marca} {self.modelo}"

class Auto(Vehiculo): # Clase hija de Vehiculo
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    
    def descripcion(self):
        return f"Vehículo: {self.marca} {self.modelo} {self.puertas}"
    
class Moto(Vehiculo): # Clase hija de Vehiculo
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo
    
    def descripcion(self):
        return f"Vehículo: {self.marca} {self.modelo} {self.tipo}"

a1 = Auto("Toyota", "Corolla", 4)
m1 = Moto("Yamaha", "R3", "Deportivo")
print(a1.descripcion())
print(m1.descripcion())
