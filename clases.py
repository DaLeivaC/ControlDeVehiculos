import csv

class Vehiculo ():
    def __init__(self, marca, modelo, nruedas):
        self.marca = marca
        self.modelo = modelo
        self.nruedas = nruedas
        

    def guardar_datos_csv (self):
        try:
            with open ("vehiculos.csv", "a", newline ="") as archivo:
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer (archivo)
                archivo_csv.writerows(datos)
        except FileNotFoundError:
            print ("No existe el archivo vehiculos.csv")
        except Exception as e:
            print ("Error reportado", e)

    
    def leer_datos_csv (self):
        try:
            with open ("vehiculos.csv", "r") as archivo:
                vehiculos = csv.reader (archivo)
                print (f"Lista de Vehiculos{type(self).__name__}")
                for item in vehiculos:
                    vehiculo_tipo = str(self.__class__)
                    if vehiculo_tipo in item [0]:
                        print (item[1])
                print ("")
        except FileNotFoundError:
            print ("No existe el archivo vehiculos.csv")
        except Exception as e:
            print ("Error reportado", e)


    
    def __str__(self):
        return f"Marca {self.marca}, modelo {self.modelo}, {self.nruedas} ruedas"
    


class Automovil(Vehiculo):
    def __init__ (self, marca, modelo, nruedas, velocidad, cilindraje):
        super().__init__(marca, modelo, nruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        return super().__str__() + f"{self.velocidad}, {self.cilindraje} cc"
    


class Particular (Automovil):
    def __init__ (self, marca, modelo, nruedas, velocidad, cilindraje, npuesto):
        super().__init__ (marca, modelo, nruedas, velocidad, cilindraje)
        self.npuesto = npuesto

    def get_npuesto(self):
        return self.npuesto
    
    def set_npuesto(self, npuesto_new ): 
        self.npuesto = npuesto_new

    def __str__(self):
        return super().__str__() + f", puestos: {self.npuesto}"
    

class Carga (Automovil):
    def __init__ (self, marca, modelo, nruedas, velocidad, cilindraje, pesodecarga):
        super().__init__(marca, modelo, nruedas, velocidad, cilindraje)
        self.pesodecarga = pesodecarga

    def __str__(self):
        return super().__str__() + f", peso de carga: {self.pesodecarga}"
    
class Bicicleta (Vehiculo):
    def __init__(self, marca, modelo, nruedas, tipo):
        super().__init__(marca, modelo, nruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f", tipo de bicicleta: {self.tipo}"
    
class Motocicleta (Bicicleta):
    def __init__(self, marca, modelo, nruedas, tipo, nradios, cuadro, motor):
        super().__init__(marca, modelo, nruedas, tipo)
        self.nradios = nradios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return super().__str__() + f", {self.nradios} radios, cuadro: {self.cuadro}, motor: {self.motor}"