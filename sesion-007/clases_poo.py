class Vehiculo:
    def __init__(self, marca, volumen_com_m3, velocidad_max_mps): # Metodo constructor
        self.marca = marca
        self.volumen_comb_m3 = volumen_com_m3
        self.velocidad_max_mps = velocidad_max_mps

    def mostrar_volumen_comb_l(self):
        volumen_comb_l = self.volumen_comb_m3*1000
        print("Volumen en L:", volumen_comb_l)
    
    def mostrar_velocidad_kmph(self):
        velocidad_kmph = self.velocidad_max_mps*3600/1000
        print("Velocidad en KM/H:", velocidad_kmph)

vehiculo1 = Vehiculo("Mazda", 0.15, 50)
vehiculo1.mostrar_velocidad_kmph()
vehiculo1.mostrar_volumen_comb_l()

vehiculo2 = Vehiculo("Mercedes", 0.078, 43)
vehiculo2.mostrar_velocidad_kmph()
vehiculo2.mostrar_volumen_comb_l()