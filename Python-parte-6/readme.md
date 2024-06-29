Para ingresar datos desde teclado o consola vamos a usar la función input
nombre = input("Ingrese su nombre: ")
mensaje = "Su nombre es "+nombre
print(mensaje)

Para unir dos o más cadenas de caracteres (strings) uso el operador +
Ejemplo:
nombre = "Federico"
edad = 24
mensaje = "Su nombre es "+nombre+" y tenés "+str(edad)+" años."

Como hago si quiero que el usuario me ingrese un número y sumarlo a otro?
Existen en python 3 funciones que sirven para convertir datos de un tipo a otro

int(texto) -> convierte el texto a entero (si se puede)
float(texto) -> convierte el texto a flotante (si se puede)
str(numero) -> convierte el número entero o flotante a string

Conclusión:
Para convertir de texto a int uso la función int(texto)
Para convertir de texto a float uso la función float(texto)
Para convertir de int a str uso la funcion str(numeroEntero)
Para converitr de float a str uso la funcion str(numeroFlotante)