# Operadores lógicos
# and, or, not

#and
#El operador and devuelve True si lo que contiene a la izquierda y a la derecha es True. Caso contrario retorna False
# and, or o not reciben como argumento el resultado de una condición.
numero = 7
flagAnd = numero > 5 and numero > 8
print(flagAnd)

#or
#El operador or devuelve True si lo que contiene a la izquierda es True o lo que contiene a la derecha es True. Caso contrario retorna False.
numero = 8
flagOr = numero < 1 or numero < 4
print(flagOr)

#Que significa que funcionen por cortocircuito??
#and:
#Si evalúa la primera condición y me da False da false
#Si evalúa la primera condición y me da True entonces evalúa la segunda condición. 
    #Si al evaluar la segunda condición me da True, entonces da true el resultado
    #Si al evaluar la segunda condición me da False, entonces da False el resultado

#or:
#Si evalúa la primera condición y me da True entonces da True.
#Si evalúa la primera condición y me da False evalúa la segunda condición:
    #Si al evaluar la segunda condición me da True, entonces da true el resultado
    #Si al evaluar la segunda condición me da False, entonces da False el resultado


edad = 17
flagEsAdolescente = edad > 13 and edad < 18
print(flagEsAdolescente)

flagHiceLaTarea = False
flagEstudieMate = False
flagPuedoSalir = flagHiceLaTarea or flagEstudieMate
print(flagPuedoSalir)

# Operador not
#El operador not devuelve el valor bool contrario al que recibe:
flagEstudieMate = True
flagNoEstudieMate = not flagEstudieMate
print(flagNoEstudieMate)