#Potencia = tasa con la que se realiza un trabajo 
# P = W/t  | W energia transformada Watt 
#          | t = tiempo
#potencia de un motor: cantidad de energia quimica o electrica 
#que puede transformar en energía mecánica

#1 caballo = 746w o 746 j/s
# w = m*g*h 

#despeje t(s) -> t = w/p
#despeje work-> P*t = w


import math


print("""
                P = W/t 
    W energia transformada Watt | t = tiempo

            1-.Potencia (w)
            2-. Trabajo (j)
            3-. Tiempo (s)
              
""")

option = int(input(" ‎Que deseas calcular? "))

def potencia():
    w = 0
    work_option = input("Tienes el valor del trabajo en joules?..  y/ n  .")
    if work_option == "Y" or work_option == "y":
        w = float(input("Ingresa el valor del trabajo: "))
    
    elif work_option == "N" or work_option == "n":
        masa = float(input("Ingresa la masa: "))
        distancia_altura = float(input("Ingresa la altura ó distancia: "))
        w = masa * distancia_altura * 9.8

    tiempo = float(input("Ingresa el tiempo (s)"))
    potencia = w / tiempo
    hp = potencia / 746
    print(f"P = {potencia}w o P = {hp} hp")

def work():
    p = float(input("Ingresa la Potencia : "))
    hp_j = int(input("Tu valor esta en 1-. Joules | 2-. Hp -> "))
    if hp_j == 2:
        p = p * 746
    elif hp_j == 1:
        p = p

    t = float(input("Ingresa el tiempo (s): "))

    work = p * t
    print(f"Valor del trabajo: {work} joules")

def tiempo():
    w = 0
    potencia = float(input("Ingresa el valor de la potencia: "))
    hp_j = int(input("Tu valor esta en 1-. watts | 2-. Hp -> "))
    if hp_j == 2:
        potencia = potencia * 746
    elif hp_j == 1:
         potencia = potencia
    else:
        print("Opción no valida")
        return 0

    work_option = input("Tienes el valor del trabajo en joules?..  y/ n  .")
    if work_option == "Y" or work_option == "y":
        w = float(input("Ingresa el valor del trabajo (j): "))

    elif work_option == "N" or work_option == "n":
        masa = float(input("Ingresa la masa: "))
        distancia_altura = float(input("Ingresa la altura ó distancia: "))
        w = masa * distancia_altura * 9.8

    else:
        print("Opción no valida")
        

    tiempo = w / potencia
    print(f"Tiempo = {tiempo} s")


if option == 1:
    potencia()

elif option == 2:
    work()

elif option ==3:
    tiempo()


