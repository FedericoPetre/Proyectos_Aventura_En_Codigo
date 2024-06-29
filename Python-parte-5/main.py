#Funcionalidades de los comentarios multilineas:
#Sirven como texto de varios renglones
#Sirven tambien para documentar constantes, variables y funciones.

#Que es documentar??
#Sería una aclaración acerca de lo que guarda la constante, variable o lo que hace la función.

PI = 3.14
"""
Se refiere a la constante matemática 3.14
"""
print(PI)

nombre = "Federico"
'''
Variable que guarda un nombre propio
'''

print(nombre)


#Demostración de que el comentario multilínea es texto

texto = '''
Esto es un
texto en
varios renglones
'''
print(texto)
print(type(texto))

texto2 = """
Esto es un
texto en
varios renglones
con comillas
dobles
"""
print(texto2)
print(type(texto2))

mensaje = "Esto es un mensaje\r\nde varias lineas"
print(mensaje)
