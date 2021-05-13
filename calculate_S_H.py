import math
class Calculate_hight_with_specific_speed:
    def __init__(self, speed):
        self.speed = speed

    def hight_value(self):
        hight = self.speed ** 2 / 2 / 9.81
        print(f"Altura = {hight}")



class Calculate_speed_at_specific_hight:
    def __init__(self,Hight_total,Hight_required):
        self.Hight_total = Hight_total
        self.Hight_required = Hight_required
        

    def speed_value(self):
    
        gravity = 9.8
        dif_h = (gravity * self.Hight_total) - (gravity * self.Hight_required)
        speed = math.sqrt(2 * dif_h)
        print(f"{speed} m/s")
        return speed


    
  
h_S = int(input("""
NOTA: ESTA FUNCION ESTA EN FASE BETA SOLO HA SIDO TESTEADA 2 VECES 
            Si te piden calcular
    "la altura a una velocidad especifica" 
                 ó 
    la velocidad a una altura especifica

    1-. Altura / distancia (m)
   2-. Velocidad (m/s)
   

"""))
if h_S == 1:
    velocidad =  float(input("Ingresa la velocidad (m/s):  "))
    especific_hight_value = Calculate_hight_with_specific_speed(velocidad)
    especific_hight_value.hight_value()

elif h_S == 2:  
    Hight_Total =  float(input("Ingresa la altura Total: "))
    Hight_required = float(input("Ingresa la altura deseada: "))
    especific_speed_value = Calculate_speed_at_specific_hight(Hight_Total, Hight_required)
    especific_speed_value.speed_value()


