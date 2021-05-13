import math
class Gravitation_kepler:
    def __init__(self):
        pass
    
    
    def fuerza_atraccion(self):
        print("""
                      Calculo de la fuerza de atracción
                      F = G * (m1 * m2 / r²)
        """)
        m1 = float(input("Ingresa la masa del cuerpo 1: "))
        m2 = float(input("Ingresa la masa del cuerpo 2: "))
        r = float(input("Ingresa la distancia entre los cuerpos: "))
        g =  6.67e-11
        f = g * (m1 * m2 / r**2)
        print(f"El valor de la fuerza de atracción es de: {f} N")

    def calculo_masa(self):
        print("""
                      Calculo de masa 
                      mr = a*(r²)/G       
        """)
        aceleracion_option = input("Tienes el valor de la fuerza de la atracción en m/s²: Y/n ")
        if aceleracion_option == "Y" or aceleracion_option == "y":
            a = float(input("Ingresa la fuerza de atraccioón del cuerpo A al B "))
        elif aceleracion_option == "N" or aceleracion_option == "n":
            newtons = float(input("Ingresa la fuerza (N) ejercida sobre el objeto: "))
            masa = float(input("Ingresa la masa del objeto(kg): "))
            a = newtons / masa

        
        r = float(input("Ingresa la distancia entre los cuerpos en metros (m)"))
        G =  0.0000000000667

        mr_0 = a * (r ** 2)
        mr_1 = mr_0 / G
        print(f"""
        La masa del objeto es: {mr_1} kg
        """)

    def kepler3(self):
        print("""
                Tercera  ley de kepler

                    T1²      R1³    
                    --   =   ---
                    T2²      R2³    

             T = periodos del planeta
             R = Distancia al cuerpo de referencia
             
        """)
        option = input("Elige el valor requerido T ó R /  o comprobar  C")


        if option == "T" or option == "t":
            T1 = float(input("Ingresa el periodo del cuerpo 1: ")) 
            R1 = float(input("Ingresa la distancia al sol del cuerpo 1: "))       
            R2 = float(input("Ingresa la distancia al sol del cuerpo 2: "))  

            T2 = (T1   / (R1 **3 / R2**3)**(1/3))
            print(f"""
            El periodo es de  = {T2} unidades de tiempo
            """)
            


        elif option == "R" or option == "r":
            T1 = float(input("Ingresa el periodo del cuerpo 1: ")) 
            T2 = float(input("Ingresa el periodo del cuerpo 2: ")) 
            R1 = float(input("Ingresa la distancia al sol del cuerpo 1: "))       
           
            R2 = (R1   / math.sqrt(T1 **2 / T2**2))

            print(f"""
            La distancia al cuerpo de referencia  = {R2} unidades de distancia 
            """)

        elif option == "C" or option == "c":
            T1 = float(input("Ingresa el periodo del cuerpo 1: ")) 
            T2 = float(input("Ingresa el periodo del cuerpo 2: ")) 
            R1 = float(input("Ingresa la distancia al sol del cuerpo 1: "))       
            R2 = float(input("Ingresa la distancia al sol del cuerpo 2: "))   
            T = math.sqrt((T1/T2)**2)
            R = ((R1/R2)**3) ** (1/3)
            print(f"""
            T: {T} = R:{R}
            """)
            if T == R and R == T:
                print("Equivalencia Verdadera")
            else:
                print("Equivalencia Falsa")

            

       
    

       
    

      

            


lib_gravitation_kepler = Gravitation_kepler()
lib_gravitation_kepler.fuerza_atraccion()





