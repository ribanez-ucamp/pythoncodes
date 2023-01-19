texto_variado = "Palabra 123 $%&&*+$"
print(type(texto_variado))

#Podemos utilizar comillas triples para que el resultado 
#nos muestre las cadenas como las hemos escrito

# print(""" 
# Dominios web baratos

# Dominios tan originales como tus ideas. \
# Registra tu dominio con IONOS y disfruta de las funciones integrales que tenemos para ofrecerte.

#     √Correo incluido 
#     √Certificado SSL   
#     √Asistencia 24/7

# """)

#Ahora veremos subscripting e indexado

# texto = 'Python'
# print(texto[0])
# print(texto[1])
# print(texto[5])
# print(texto[-1])
# print(texto[-5])
# print(texto[-6])

#Las siguientes instrucciones marcaran error, porque están fuera
# de la longitud de la cadena, que inicia con índice 0 y termina en 5

#print(texto[6])
#print(texto[-7])

# El texto ya es inmutable, podemos tomar secciones o letras de la cadena
# para armar otras, pero, hasta este punto es irremplazable

#texto[0] = 'p' # La redefinición no es permitida, es un error

# letra = texto[0]

# print("letra")
# print(letra)

# letras_cent = texto[2:5]

# print("Las tres letras centrales son")
# print(letras_cent)

# letra = 'p'
# print("letra substituida")
# print(letra)

# texto_compuesto = letra + texto[1] # Concatenación
# print(texto_compuesto)

#######################################################

# Slicing o substringing

texto = "Python"

print(texto[0:3]) # Impresión del índice 0 al 3
print(texto[0:-3])
print(texto[0:-2])
print(texto[2:]) #Impresión desde el índice 2 hasta el final de la cadena
print(texto[:4]) #Impresión desde el índice 0 hasta el índice 4

print(texto[-3::-1]) #Impresión desde el índice -3 (hty) hasta el índice -1 después de y, es decir P 
print(texto[::-1])   #Impresión desde el principio de la cadena, regresando índice por índice (-1)
                     #hasta el fin de la cadena

#Slicing sirve para imprimir elementos dentro de la cadena y fuera de ella
 
print(texto[1:50])

print(texto[2:2])

#######################################################

# Cadenas y formatos

texto = "Hola mundo! Buenastardes"

print(texto.lower())
print(texto.upper())
# print(texto)

# texto = texto.upper()

# print(texto)

# Otros métodos

print(texto.capitalize())   #Primera letra de la cadena en mayusculas y el resto en minúsculas
print(texto.title())        #La primera letra de cada palabra en la cadena es mayúscula
print(texto.swapcase())     #Intercambia mayúsculas por minúsculas y viceversa

#Formato con parámetros

print('{} + {} = {}'.format(2, 3, 2+3)) # En estos ejemplos, se definen parámetros de diferentes tipos
print('{} + {} = {}'.format("Hola", "mundo", "Hola mundo")) # y en diferente orden
print('{:3f} + {:4f} = {}'.format(2, 3, 2+3))               # para ver los diferentes efectos
print('{1} + {0} = {2}'.format(2, 3, 2+3))
print('{1} + {0} = {2}'.format("mundo", "Hola", "Hola mundo"))

#Sistemas numéricos

print('{:d} = {:b} = {:o} = {:x}'.format(15, 15, 15, 15))

input()