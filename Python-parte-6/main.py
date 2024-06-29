#Para ingresar datos desde teclado o consola vamos a usar la función input
'''
nombre = input("Ingrese su nombre: ")
mensaje = "Su nombre es "+nombre
print(mensaje)
'''
'''
numeroIngresado = input('Ingrese un número: ')
suma = 10 + int(numeroIngresado) #Fuertemente tipado en Python
print(suma)
'''
#Como soluciono esto? Si quiero que el usuario me ingrese un número y sumarlo a otro?
#Existen en python 3 funciones que sirven para convertir datos de un tipo a otro
'''
#int
numero = int("4")
print(numero)
print(type(numero))

#float
numero_flotante = float('7.5')
print(numero_flotante)
print(type(numero_flotante))

#str
numeroEnTexto = str(3)
print(numeroEnTexto)
print(type(numeroEnTexto))

#conclusión:
#Para convertir de texto a int uso la función int(texto)
#Para convertir de texto a float uso la función float(texto)
#Para convertir de int a str uso la funcion str(numeroEntero)
#Para converitr de float a str uso la funcion str(numeroFlotante)

numeroEnTextoFloat = str(3.5)
print(numeroEnTextoFloat)
print(type(numeroEnTextoFloat))
'''

# Que pasa si quiero incluir un float, o un entero dentro de una cadena de caracteres (string)
numeroFloat = 3.5
mensaje = "El numero flotante es: "
print(mensaje)

#Para el próximo video vamos a ver los famosos f-strings