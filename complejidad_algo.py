import time

def factorial_ite(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_rec(n):
    if n == 1:
        return 1
    
    return n * factorial_ite(n - 1)


if __name__ == "__main__":
    n = 150000

# Utilizamos el módulo time y el método time para comparar cuanto tarda una función en resolverse:

    comienzo = time.time()
    factorial_ite(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_rec(n)
    final = time.time()
    print(final - comienzo)


