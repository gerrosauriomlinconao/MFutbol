from random import randint

from Jugadores.Jugador import Jugador


class Delantero(Jugador):
    pass


    def __init__(self):
        Jugador.__init__(self)
        self.posicion = "Delantero"
        self.gambeta = randint(65, 88)
        self.calidadTirosDeFalta = randint(67, 95)
        self.potenciaTiro = randint(75, 95)
        self.velocidad = randint(70, 90)
        self.resistencia = randint(65, 90)
        self.agresividad = randint(67, 90)
        self.pase = randint(65, 90)
        self.cabezaso = randint(70, 87)
        self.inteligencia = randint(70, 87)


    def get_media(self):
        sum = self.calidadTirosDeFalta + self.gambeta + self.potenciaTiro + self.velocidad
        sum += self.resistencia + self.agresividad + self.pase +  self.cabezaso
        return sum // 8

    def getPosesionPelota(self):
        sum = self.velocidad + self.resistencia + self.pase + self.inteligencia
        return sum // 4