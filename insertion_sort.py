# Ejercicio para generar un algoritmo de ordenamiento por inserción - Insertion Sort del curso de POO con Python de Platzi

import random

def ordena_insercion(lista):
    n = len(lista)
    

    for indice in range(1, n):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual -1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
        
        lista[posicion_actual] = valor_actual

    return lista

if __name__ == "__main__":

    tamano_lista = int(input("Cuántos elementos tendrá la lista: "))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)

    lista_ordenada = ordena_insercion(lista)
    print(lista_ordenada)