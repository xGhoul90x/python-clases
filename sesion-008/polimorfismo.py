class Persona:
    def __init__(self, nombre = None, anho_nac = None, estatura_cm = None):
        self.nombre = nombre
        self.anho_nac = anho_nac
        self.estatura_cm = estatura_cm
    
    def print(self, saludo = ""):
        if saludo != "":
            print(saludo, self.nombre)
        print("Nombre:", self.nombre)
        print("Anho de nac.:", self.anho_nac)
        print("Estatura en cm:", self.estatura_cm)
    
    def get_nombre(self):
        return self.nombre

    def get_anho_nac(self):
        return self.anho_nac
    
    def get_estatura_cm(self):
        return self.estatura_cm
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_anho_nac(self, anho_nac):
        self.anho_nac = anho_nac

    def set_estatura_cm(self, estatura_cm):
        self.estatura_cm = estatura_cm

p1 = Persona("Jose")
p1.set_anho_nac(2000)
p1.set_estatura_cm(191)
p1.print("Buenos días")
