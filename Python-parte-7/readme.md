Los f-strings se usan para formatear strings con variables, es decir, incluir los valores de las variables dentro de un string
sin la necesidad de convertir tipos de datos y tampoco usar los operadores de concatenación.

se usan anteponiendo la letra f (minúscula o mayúscula) al string, y pasándole entre llaves {} la expresión (constante, variable, condición o resultado de una función).

Ejemplo:
nombre = "Federico"
edad = 24
pais = "Argentina"

mensaje = f"Su nombre es {nombre}, tenés {edad} años y vivís en {pais}"
print(mensaje)

Si quisieramos que se vea en varios renglones, usamos los comentarios multilíneas (con comillas simples o dobles y anteponiendo la letra f al texto). 

Ejemplo:
PI = 3.14
numeroEntero = 10
numeroFlotante = 3.5
texto = "Hola, como estas??"

mensaje = f"""La constante es {PI}
El número entero es {numeroEntero}
El número flotante es {numeroFlotante}
El valor lógico es {numeroEntero <= 9}
El texto es {texto}"""