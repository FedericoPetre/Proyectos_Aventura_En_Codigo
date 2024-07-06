nombre = "Federico"
edad = 24
pais = "Argentina"
'''
'''

'''
#El operador + de concatenación sirve para unir dos o más textos
mensaje = "Nombre: "+nombre+"\nEdad: "+str(edad)+" años\nNacionalidad: "+pais+"\n\n"
print(mensaje)

#Ejemplo del mismo caso con uso de f-strings
mensaje2 = f'Su nombre es {nombre}, tenés {edad} años y vivís en {pais}'
print(mensaje2)

PI = 3.14
numeroEntero = 10
numeroFlotante = 3.5
texto = "Hola, como estas??"

mensaje = f"""La constante es {PI}
El número entero es {numeroEntero}
El número flotante es {numeroFlotante}
El valor lógico es {numeroEntero <= 9}
El texto es {texto}"""

print(mensaje)

texto = "."
textoABool = bool(texto)
print(textoABool)
'''