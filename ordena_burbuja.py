# Ejercicio de un algoritmo de ordenamiento tipo burbuja del curso de POO con Python de Platzi.

# Complejidad Algorítmica: O(n) * O(n -i -1)= O(n**2)


import random

def ordenamiento_burbuja(lista):
    n = len(lista)    #Obtenemos la longitud de la lista

    for i in range(n):    
        for j in range(0, n - i - 1): # Recorrer la lista hasta el índice final[n] menos [i - 1] (el índice final menos uno).

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# La notación en Python para intercambiar y reasignar se llama swapping

if __name__ == "__main__":
    elementos_en_lista = int(input("Cuántos elementos tendrá la lista: "))

    lista = [random.randint(0, 100) for i in range(elementos_en_lista)]
    print(lista)

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)