# Tema herencia, clase del curso de POO con Python de Platzi

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base 
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):   # Definir el nombre de la superclase
                              # Se lee como: la clase Cuadrado extiende a Rectangulo

    def __init__(self, lado):
        super().__init__(lado, lado)  # Función super() permite obtener una referencia directa de la superclase. Llamamos a su constructor. 
        # Cuando inicializamos una subclase necesitamos inicializarla con su constructor.


if __name__ == "__main__":
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())
