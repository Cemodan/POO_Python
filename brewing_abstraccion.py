# Ejercicio para realizar la abstracción de la elaboración de cerveza

class Molienda:

    def __init__(self):
        pass

    def moler(self, grado_molido = "normal"):
        self._pesar_maltas()
        self._preparar_molino()
        self._agregar_maltas_al_molino()
        self._ajustar_grado_molienda(grado_molido)
        self._recuperar_malta_molida()
        

    def _pesar_maltas(self):
        print("\n\t> Maltas pesadas")
    
    def _preparar_molino(self):
        print("\n\t> Molino limpio y listo")

    def _agregar_maltas_al_molino(self):
        print("\n\t> Maltas listas para moler")

    def _ajustar_grado_molienda(self, grado_molido):
        print(f'\n\t> Molino ajustado para la molienda grado > {grado_molido}')
    
    def _recuperar_malta_molida(self):
        print("\n> Maltas listas para la maceración")

class Macerado:

    def __init__(self):
        pass

    def maceracion(self, temp="67ºC", mash_out="78ºC", pH=5.6, tiempo_macerado="60 min", almidon=True):
        self._calentar_agua(temp)
        self._ajustar_ph(pH)
        self._agregar_maltas()
        self._maceracion(tiempo_macerado)
        self._prueba_almidon(almidon)
        self._fin_macerado(mash_out)
        self._clarificacion()
        self._trasvase()

    def _calentar_agua(self, temp):
        print(f'\n\t> Agua lista para macerar a una temperatura de {temp}')
    def _ajustar_ph(self, pH):
        print(f'\n\t> pH ajustado a {pH}')
    def _agregar_maltas(self):
        print(f'\n\t> Maltas molidas agregadas')
    def _maceracion(self,tiempo_macerado):
        print(f'\n\t> Macerando las maltas.')
    def _prueba_almidon(self,almidon):
        print(f'\n\t> Prueba de almido = {almidon}')
    def _fin_macerado(self, mash_out):
        print(f'\n\t> Terminando maceración, elevando temperatura a {mash_out}')
    def _clarificacion(self):
        print(f'\n\t> Clarificando el mosto mediante recirculación')
    def _trasvase(self):
        print(f'\n\t> Mandado el mosto al tanque de hervor')

class Hervido:

    def __init__(self):
        pass

    def hervor(self, temp_h="92.5ºC", duracion="60 min", first_wort="80ºC"):
        self._abrir_vapor()
        self._elevar_temperatura()
        self._agregar_lupulos_amargor(first_wort)
        self._inicio_hervor(temp_h)
        self._fin_hervor(duracion)
        print(f'\n\t> Hervor terminado con una duración de {duracion} y adición de lúpulo en first wort de {first_wort}')

    def _abrir_vapor(self):
        pass
    def _elevar_temperatura(self):
        pass
    def _agregar_lupulos_amargor(self, first_wort):
        pass
    def _inicio_hervor(self, temp_h):
        pass
    def _fin_hervor(self, duracion):
        pass


class Whirlpool:

    def __init__(self):
        pass

    
    def whirlpool(self):
        self._whirlpool_init()

    def _whirlpool_init(self):
        print('\n\t > Whirlpool Terminado')


class Fermentacion:

    def __init__(self):
        pass

    def fermentacion(self, temp_f="18ºC", duracionf="8 días", cold_crash="1ºC", carb="2.5 atm"):
        self._ajustar_tempf(temp_f)
        self._inocular_levadura()
        self._proceso_de_fermentacion(duracionf)
        self._clarificacion(cold_crash)
        self._carbonatacion(carb)

    def _ajustar_tempf(self, temp_f):
        print(f'\n\t > Temperatura ajustada a {temp_f} para fermentación')
    def _inocular_levadura(self):
        print(f'\n\t > Se realizó el pitching con la levadura elegida')
    def _proceso_de_fermentacion(self, duracionf):
        print(f'\n\t > Dejamos fermentar durante {duracionf}')
    def _clarificacion(self, cold_crash):
        print(f'\n\t > Proceso de clarificación terminó con un cold crash a una temperatura de {cold_crash}')
    def _carbonatacion(self, carb):
        print(f'\n\t > Terminada la clarificación procedemos a carbonatar la cerveza a {carb}')



if __name__ == "__main__":
    print(f'\n> Preparando la materia prima para la maceración:')
    cocinando = Molienda()
    cocinando.moler()
    print(f'\n\nIniciando el proceso de macerado:')
    macerando = Macerado()
    macerando.maceracion()
    print(f'\n\n Iniciando el hervido del mosto...')
    hirviendo = Hervido()
    hirviendo.hervor()
    print(f'\n\n Hervor terminado, iniciando Whirlpool...')
    whirlpooling = Whirlpool()
    whirlpooling.whirlpool()
    print(f'\n\n Iniciando proceso de Fermentación...')
    fermentando = Fermentacion()
    fermentando.fermentacion()
    print(f'''\n\n >>>¡Viva! haz terminado el proceso de elaboración de cerveza<<<
    
    \tAhora puedes beber directo del fermentador
    
    \t\t\t¡Salud!\n\n''')

    