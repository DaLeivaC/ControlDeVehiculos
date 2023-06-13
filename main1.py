from clases import Automovil

instancias = []

n = int (input("¿Cuántos vehículos desea agregar? => "))

for i in range (n):
    print(f"Datos del automóvil {i+1}")
    marca = input ("Inserte la marca del automóvil: ")
    modelo = input ("Inserte el modelo: ")
    nruedas = int (input ("Inserte el número de ruedas del vehículo: "))
    velocidad = int (input ("Inserte la velocidad del vehículo en km/h: "))
    cilindraje = int (input ("Inserte el cilindraje del vehículo en cc: "))

    print ("")

    auto = Automovil (marca, modelo, nruedas, velocidad, cilindraje)
    instancias.append(auto)

print ("Imprimiendo por pantalla los vehículos ==> ")

for index,item in enumerate(instancias):
    print (f"Datos del automovil {index + 1} : Marca {item.marca}, Modelo {item.modelo}, {item.nruedas} ruedas, {item.velocidad} km/h, {item.cilindraje} cc")