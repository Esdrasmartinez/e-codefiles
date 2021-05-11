#           "Trabajo, energía y potencia"
#             Formula = Ec = 1/2 * m* v2 
#  Ec = evergia cinetica  | m  = masa (kg) | v = velocidad m/s
import math

#-
print("""
----------Trabajo, energía y potencia--------------
            1-. Energia Cinetica 
                  2-. Masa
               3-. Velocidad 
               ---------------
""")

option = int(input("Elige una opcion: "))

def cinetic_energy():
    masa = float(input("Ingresa la masa: "))
    velocidad = float(input("Ingresa la velocidad: "))
    energia_cinetica = 0.5 * masa * velocidad **2
    print(f"{energia_cinetica} joules")


def masa():
    energia_cinetica = float(input("Ingresa la energia cinetica: "))
    velocidad = float(input("Ingresa la velocidad: "))
    masa = 2 * (energia_cinetica / velocidad **2)
    print(f"{masa} kg")



def velocidad():
    energia_cinetica = float(input("Ingresa la energia cinetica: "))
    masa = float(input("Ingresa la masa: "))
    velocidad = math.sqrt(energia_cinetica / (masa / 2))
    print(f"{velocidad} m/s")


if option == 1:
    cinetic_energy()
elif option == 2:
    masa()
elif option == 3:
    velocidad()


