import random

def juego_adivinanza():
numero_secreto = random.randint(1,100)
#uso de la libreria random y el randit usa numero sin decimales
intentos = 0
adivinado = False

print("Bienvenid@ al juego de adivinanza de numeros")
print("Escribe un numero del 1 al 100")

while not adivinado:
    prueba = int(input("Adivina el numero:"))
    intentos +=1

 
    if prueba < numero_secreto:
        print("Ingresa un numero mayor"
    elif prueba > numero_secreto
        print("Ingresa un numero menor")
    else:
        adivinado = True
        print(f"Felicidades! Adivinaste el numero secreto!!!")
juego_adivinanza()