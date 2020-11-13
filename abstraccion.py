# Clase "Abstracción" del curso POO con Python de Platzi
# Ejemplo de elaboración de variables y métodos privados para abtraerlos del usuario.

# Creamos la clase lavadora:
class Lavadora:

    def __init__(self):
        pass
   # Tiene un método público lavar que referencia a otros métodos privados: 
    def lavar(self, temperatura="caliente"): 
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()
        self._enjuagar()
        self._centrifugado_2()
    
# Los métodos privados de la clase no son relevantes para el uso desde afuera de la clase y por convención inician con _

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')
    
    def _anadir_jabon(self):
        print(f'Anadiendo jabon')

    def _lavar(self):
        print(f'Lavando la ropa sucia')

    def _centrifugar(self):
        print(f'Este es el centrifugado del lavado')

    def _enjuagar(self):
        print('Enjuagando la ropa limpia')

    def _centrifugado_2(self):
        print('Centrifugado por segunda ocasión para quitar agua de enjuague')

if __name__ == "__main__":
    lavadora = Lavadora() # Creando instancia de lavadora
    lavadora.lavar() # Ejecutando la acción (método público) de la instancia
    print("\nEstrenando o vel rosita")