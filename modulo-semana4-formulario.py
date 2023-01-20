#Formulario simple
nombre = input("Por favor, introduce tu nombre: ")
apellido_p = input("Introduce tu apellido paterno: ")
apellido_m = input("Introduce tu apellido materno: ")
edad = int(input("Introduce tu edad: "))
correo = input("Introduce tu e-mail: ")
telefono = input("Introduce tu teléfono: ")

print("Nombre: " + nombre)
print("Apellido paterno: " + apellido_p)
print("Apellido materno: " + apellido_m)
#print("Tengo: " + edad) #ERROR
print("Tengo: " + str(edad) + " años")
print("Correo: " + correo)
print("Teléfono: " + telefono)

input()
