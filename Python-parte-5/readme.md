Funcionalidades de los comentarios multilineas:
Sirven como texto de varios renglones
Sirven tambien para documentar constantes, variables y funciones.

Que es documentar??
Sería una aclaración acerca de lo que guarda la constante, variable o lo que hace la función.

Ejemplos:

PI = 3.14
"""
Se refiere a la constante matemática 3.14
"""

nombre = "Federico"
'''
Variable que guarda un nombre propio
'''


Demostración de que el comentario multilínea es texto

texto = '''
Esto es un
texto en
varios renglones
'''
print(texto)
print(type(texto))

Salto de línea en texto: \n
Retorno de carro en texto: \r
