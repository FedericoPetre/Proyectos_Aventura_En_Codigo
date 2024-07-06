Estrucutras de control condicional
Sintaxis de la estructura de control condicional if (simples)

if condicion:
    bloque de instrucciones que se ejecutan si la condicion es True

Ejemplos:

1- 
nota = int(input("Ingrese una nota entre 1 y 10: "))
if nota >= 7 :
    print("El alumno aprobó")

print("Continúa con las instrucciones normales del programa")

print("Fin del programa.")


2-
flagHiceLaTarea = False
flagEstudieMate = True

if flagHiceLaTarea or flagEstudieMate:
    print("Podés salir")

print("Continúa con las instrucciones normales del programa")
print("Fin del programa.")