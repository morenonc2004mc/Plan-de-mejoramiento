#Ejercicio 1 - Programe una función que determine si dos listas son iguales. Dos listas se
#consideran iguales si tienen igual longitud y sus elementos en cada índice
def lista_igual(lista1, lista2):
	if lista1 == lista2:
		return("Son iguales. ")
	else:
		return("Son diferentes. ")
lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
print(lista_igual(lista1, lista2))

#Ejercicio 2
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , 14, 15]
print(lista[2:15])
print(lista[2:15:2])
print(lista[2:15:3])

#Ejercicio 3
#Escriba un programa en python que acepte una lista y que elimine los elementos duplicados 
#Clase definida para representar los conjuntos 
lista = [1, 2, 3, 11, 15, 20, 15, 20, 90, 90, 80, 87, 11]
print(lista)
conjunto=set()
conjunto=set(lista)
lista=list(conjunto)
lista.sort()
print(conjunto)

#Ejemplo 4
import random
lista = []
rango = random(random.random()*100)
print(rango)





 
