Operadores relacionales (o de comparación):
Siempre retornan un bool (True o False)
Listado de operadores relacionales:

1- Operador mayor que (>)
Devuelve True si lo que se encuentra a la izquierda es mayor a lo que se encuentra a la derecha

2- Operador mayor o igual que (>=)
Devuelve True si lo que se encuentra a la izquierda es mayor o igual a lo que se encuentra a la derecha

3- Operador menor que (<)
Devuelve True si lo que se encuentra a la izquierda es menor (estricto) a lo que se encuentra a la derecha. Caso contario retorna False

4- Operador menor o igual que (<=)
Devuelve True si lo que se encuentra a la izquierda es menor o igual a lo que se encuentra a la derecha. Caso contario retorna False

5- Operador es igual (==)
Devuelve True si lo que se encuentra a la izquierda es igual (en valor y si el tipo de dato es el mismo (numérico con numérico o string con stirng o bool con bool)) a lo que se encuentra a la derecha. Caso contrario retorna False.
Ejemplo:
flagEsIgualQue = 24 == 24 #Devuelve True
flagEsIgualQue = 24 == 24.0 #Devuelve True
flagEsIgualQue = 24 == "24" #Devuelve False
flagEsIgualQue = "Fede" == 'Fede' #Devuelve True
flagEsIgualQue = "Fede" == 'FEde' #Devuelve False
flagEsIgualQue = True == True #Devuelve True
flagEsIgualQue = False == False #Devuelve True
flagEsIgualQue = True == False #Devuelve False


Operador es distinto que (!=)
Devuelve True si lo que se encuentra a la izquierda es distitno (en valor o tipo de dato (numérico con numérico o string con stirng o bool con bool)) a lo que se encuentra a la derecha. Caso contrario retorna False.
Ejemplo:
flagEsDistintoQue = 24 != 24 #Devuelve False
flagEsDistintoQue = 24 != 24.0 #Devuelve Flase
flagEsDistintoQue = 24 != "24" #Devuelve True
flagEsDistintoQue = "Fede" != 'Fede' #Devuelve False
flagEsDistintoQue = "Fede" != 'FEde' #Devuelve True
flagEsDistintoQue = True != True #Devuelve False
flagEsDistintoQue = False != False #Devuelve False
flagEsDistintoQue = True != False #Devuelve True


Constantes: Las constantes son un tipo de dato, cuyo valor no va a cambiar a lo largo del programa, y por consecuente durante su ejecución.
Se suelen declarar en mayúscula y sirve para indicarle al programador y al programa que eso se trata de una constante.
Ejemplo:
PI = 3.14