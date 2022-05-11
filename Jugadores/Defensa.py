from random import randint

from Jugadores.Jugador import Jugador


class Defensor(Jugador):
    pass


    def __init__(self):
        Jugador.__init__(self)
        self.posicion = "Defensa"
        self.marca = randint(40, 95)
        self.gambeta = randint(55, 84)
        self.calidadTirosDeFalta = randint(62, 80)
        self.potenciaTiro = randint(60, 80)
        self.velocidad = randint(65, 90)
        self.resistencia = randint(70, 90)
        self.agresividad = randint(70, 90)
        self.pase = randint(35, 86)
        self.potenciaTiro = randint(50, 90)
        self.inteligencia = randint(45, 90)

    def get_media(self):
        sum = self.marca + self.gambeta + self.calidadTirosDeFalta + self.potenciaTiro
        sum += self.velocidad + self.resistencia + self.agresividad + self.pase + self.potenciaTiro + self.inteligencia
        return sum // 11

    def getPosesionPelota(self):
        sum = self.marca + self.velocidad + self.resistencia + self.pase + self.inteligencia
        return sum // 5