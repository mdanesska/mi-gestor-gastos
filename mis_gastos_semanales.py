#Lista de Gastos Semanales

gastos = [10, 35, 100, 50, 30, 50]
total = sum(gastos)
print(f"El total de tus gastos semanales es: {total}")

# Promedio de gastos
promedio = total / len(gastos)
print(f"El promedio de tus gastos semanales es: {promedio}")

#Gastos mayores a 20 euros
gastos_mayores = []  # Lista vacía para guardar los resultados

for x in gastos:
    if x > 20:
        gastos_mayores.append(x)
    print(f"Gastos mayores a 20 euros: {gastos_mayores}")    

total_gastos_mayores = sum(gastos_mayores)

promedio_gastos_mayores = total_gastos_mayores / len(gastos_mayores)
print(f"El promedio de tus gastos mayores a  euros es: {promedio_gastos_mayores} euros")

if promedio > 100:
    print("Tus gastos semanales exceden tu presupuesto de 100Euros")

else:
    if promedio < 50:
        print("Felicidades, no estas gastando demasiado :D")