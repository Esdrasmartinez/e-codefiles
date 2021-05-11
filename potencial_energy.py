import cssh_lib
import math

class potencial_energy:
    def __init__(self):
        pass
    def potencia_energy(self):
        masa = float(input("Ingresa la masa: "))
        altura = float(input("Ingresa la altura relativa: "))
        if altura == abs(altura):
            negative_option = input("La altura es positiva?  Y/n...")
            if negative_option == "Y" or negative_option == "y":
                altura = altura 
            elif negative_option == "N" or negative_option == "n":
                altura = altura * -1
        Pe = masa * altura * 9.8
        
        cache = [masa,altura,Pe]
        return cache


potencial_energy_calculate = potencial_energy()
PE_values = potencial_energy_calculate.potencia_energy()
print(f"{PE_values[2]} joules")
