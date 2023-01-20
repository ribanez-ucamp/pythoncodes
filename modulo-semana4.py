numHuevos = 12

#Error de sintaxis
#print('Tengo ' + numHuevos + ' huevos.')

#Y error en tiempo de ejecución
#Opción 1
# print("Opción 1")
# print('Tengo ' + str(numHuevos) + ' huevos.')

#Opción 2
# print("Opción 2")
# print('Tengo  %s  huevos.' %(numHuevos))

#Opción 3
# print("Opción 3")
# print(f"Tengo  {numHuevos} huevos.")

#Error de lógica

#Calcular la superficie o área de un cuadrado

lado = int(input("Ingrese la medida del lado del cuadrado: "))

print("error")
superficie = lado * lado * lado
print(superficie)

print("correcto")
superficie_ok = lado * lado
print("La superficie del cuadrado es: " + str(superficie_ok))
input()
