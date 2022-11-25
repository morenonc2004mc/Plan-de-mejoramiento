#Ejercicio 1
#Escribir un programa que permita generar  la tabla de multiplicar de un numero entero positivo N, comenzando desde 1
#Si el usuario escribe un numero incorrecto, el programa no se ejecuta. En cambio,
#Pregunta de nuevo por la informacion hasta que el dato ingresado sea correcto.
"""comprobar = True 
while True:

	n = int(input("Ingrese un numero entero positivo: "))
	if n > 0:
		for i in range(1,11):
			print(n, "por", i, "es igual a:", n*i)

		comprobar = False 
	else:
		print("El numero ingresado no es correcto. Intentelo nuevamente")"""

#Ejercicio 2
#Crear un programa que lea un numero entero positivo N y escriba todos los numeros primos menores a dicho numero 
#Creciente que va a ir desde el numero dos hasta el numero anterior en el que este el iterador i
"""n = int(input("Ingrese un numero entero positivo: "))
if n > 0:
	for i in range(2,n):
		creciente = 2
		esPrimo = True

		while esPrimo and creciente < i:
			if i % creciente == 0:
				esPrimo = False 
			else:
				creciente += 1
		if esPrimo:
			print(i, "Es primo.")"""	


#Ejercicio 3
#Construir un programa que al recibir como datos al peso la altura y el genero de N personas que pertenecen al estado de un pais
#obtenga el promedio de peso y el promedio de la altura, tanto la poblacion masculina com femenina.
n = int(input("Ingrese la cantidad de personas a evaluar: "))
if n > 0:
	peso_hombres = 0
	altura_hombres = 0
	peso_mujeres = 0
	altura_mujeres = 0
	cantidad_hombres = 0 
	cantidad_mujeres = 0
	
	for i in range(n): 
		print(i)







#Ejercicio 4
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""word = input("Introduce una palabra: ")
#for i in range(10):
    #print(word)"""

#Ejercicio 5
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
