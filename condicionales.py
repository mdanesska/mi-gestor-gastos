
    #Cine da descuento segun edad

edad = int(input("¿Que edad tiene? "))

if edad < 0:
    # gratis
    print("Inserte edad valida")

elif edad < 5:
    # gratis
    print("Valor de entrada es 0 euros")
elif edad < 17:
    # descuento de estudiantes 5 euros
    print("Valor de entrada es 5 euros")
elif edad < 64:
    # Entrada general 17 euros
    print("Entrada general 17 euros")
else:
    # descuento adulto mayor 4 euros
    print("Adulto Mayor 4 euros")