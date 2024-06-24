EDAD = 24

#Operadores relacionales (o de comparación):
#Siempre retornan un bool (True o False)
#Listado de operadores relacionales:
# Operador mayor que (>)
# Operador mayor o igual que (>=)
# Operador menor que (<)
# Operador menor o igual que (<=)
# Operador es igual (==)
# Operador es distinto que (!=)

# Operador mayor que (>) Devuelve True si lo que se encuentra a la izquierda es mayor a lo que se encuentra a la derecha
flagEsMayorQue = EDAD > 24 #False
print(flagEsMayorQue)

# Operador mayor o igual que (>=)
#Devuelve True si lo que se encuentra a la izquierda es mayor o igual a lo que se encuentra a la derecha
flagEsMayorOIgualQue = EDAD >= 24
print(flagEsMayorOIgualQue)

# Operador menor que (<)
# Devuelve True si lo que se encuentra a la izquierda es menor (estricto) a lo que se encuentra a la derecha. Caso contario retorna False
flagEsMenorQue = EDAD < 18 # False
print(flagEsMenorQue)

# Operador menor o igual que (<=)
# Devuelve True si lo que se encuentra a la izquierda es menor o igual a lo que se encuentra a la derecha. Caso contario retorna False
flagEsMenorOIgualQue = EDAD <= 24 # True
print(flagEsMenorOIgualQue)

# Operador es igual (==)
# Devuelve True si lo que se encuentra a la izquierda es igual (en valor) a lo que se encuentra a la derecha. Caso contrario retorna False.
flagEsIgualQue = EDAD == 24 
print(flagEsIgualQue) #True

flagEsIgualQue = EDAD == 24.0
print(flagEsIgualQue) #True

flagEsIgualQue = EDAD == "24"
print(flagEsIgualQue) #False

flagEsIgualQue = False == False
print(flagEsIgualQue)

flagEsIgualQue = "Fede" == 'Fede' #Para que devuelva True los string que compare tiene que estar escritos idénticamente
print(flagEsIgualQue) #True

flagEsIgualQue = "Fede" == "fede" 
print(flagEsIgualQue) #False


# Operador es distinto que (!=)
# Devuelve True si lo que está la izquierda es distinto a lo que se encuentra a la derecha (en valor)

flagEsDistintoQue = EDAD != 24 
print(flagEsDistintoQue) #False

flagEsDistintoQue = EDAD != 24.0
print(flagEsDistintoQue) #False

flagEsDistintoQue = EDAD != "24"
print(flagEsDistintoQue) #True

flagEsDistintoQue = False != False
print(flagEsDistintoQue) #False

flagEsDistintoQue = "Fede" != 'Fede' #Para que devuelva True los string que compare tiene que estar escritos idénticamente
print(flagEsDistintoQue) #False

flagEsDistintoQue = "Fede" != "fede" 
print(flagEsDistintoQue) #True

#Observación: Siempre que sean los mismos valores que les pasamos al operador == y al operador !=, 
#Un operador va a devolver lo contrario (lo opuesto) que el otro.

calculoCombinado = 5*1.5 + 1
print(calculoCombinado)
flagEdadEsMayorQueElResultadoDeLaOperacion = EDAD > calculoCombinado
print(flagEdadEsMayorQueElResultadoDeLaOperacion)
