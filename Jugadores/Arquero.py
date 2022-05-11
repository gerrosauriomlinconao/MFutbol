from random import randint

from Jugadores.Jugador import Jugador


class Arquero(Jugador):
    pass


    def __init__(self):
        Jugador.__init__(self)
        self.posicion = "Arquero"
        self.marca = randint(30, 57)
        self.velocidad = randint(60, 90)
        self.resistencia = randint(67, 90)
        self.agresividad = randint(50, 90)
        self.pase = randint(55, 90)
        self.potenciaTiro = randint(50, 90)
        self.manoAMano = randint(75, 95)
        self.tirosDeFalta = randint(75, 90)
        self.penales = randint(60, 90)
        self.agilidad = randint(75, 90)

    def getPosesionPelota(self):
        return 1

    def get_media(self):
        sum = self.marca + self.potenciaTiro + self.velocidad + self.resistencia + self.agresividad + self.pase
        sum += self.potenciaTiro + self.manoAMano + self.tirosDeFalta + self.penales + self.agilidad
        return sum // 11

