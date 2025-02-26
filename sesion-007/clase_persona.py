class Persona:
    def __init__(self, nombre, anho_nac, estatura_cm):
        self.nombre = nombre
        self.anho_nac = anho_nac
        self.estatura_cm = estatura_cm
    
    def print(self):
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

personas = []
persona1 = Persona("Jose", 1998, 173)
personas.append(persona1)
persona2 = Persona("Juan", 1997, 172)
personas.append(persona2)
persona3 = Persona("Luis", 1996, 171)
personas.append(persona3)
print(personas)
print(personas[2].get_anho_nac())
personas[2].set_anho_nac(2000)
print(personas[2].get_anho_nac())