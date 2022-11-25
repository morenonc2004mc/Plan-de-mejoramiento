#Ejercicio 1. 
"""x = float(input("Ingrese un numero: "))
y = float(input("Ingrese un numero: "))
if x > y:
	print(x,"es mayor que",y)
elif x < y:
	print(x,"es menor que",y)
else:
	print("Son iguales")"""

#Ejercicio 2
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es menor de edad o no.
"""edad = int(input("¿Cuantos años tienes: "))
if edad > 17:
	print("Eres mayor de edad")
else:
	print("Eres menor de edad")"""

# Ejercicio de ejemplo 3
"""x = int(input("Ingresa un entero, porfavor: "))
if x < 0:
	x = 0
	print("Negativo cambiado a cero")
elif x == 0:
	print("cero")
elif x == 1:
	print("Simple")
else:
	print("Mas")"""

# Ejercicio 4 
"""numero = int(input("Introduce un numero entero: "))
if numero % 2 == 0:
	print("El numero" + str(numero) + "Es par")
else:
	print("El numero\n" + str(numero) + "Es impar")"""


#Ejercicio 5
#Si un numero es divisor de otro
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
if n1 % n2 == 0:
	print(n2, "Es divisor de", n1)
else:
	print(n2, "No es divisor de", n1)
	
