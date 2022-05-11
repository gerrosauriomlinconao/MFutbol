from random import randint

from Jugadores.Jugador import Jugador


class Volante(Jugador):
    pass


    def __init__(self):
        Jugador.__init__(self)
        self.posicion = "Volante"
        self.marca = randint(60, 85)
        self.gambeta = randint(65, 90)
        self.calidadTirosDeFalta = randint(75, 95)
        self.potenciaTiro = randint(55, 88)
        self.velocidad = randint(50, 90)
        self.resistencia = randint(65, 90)
        self.agresividad = randint(50, 90)
        self.pase = randint(75, 90)
        self.habilidad = randint(75, 90)



    def get_media(self):
        sum = self.marca + self.gambeta + self.calidadTirosDeFalta + self.potenciaTiro + self.velocidad + self.resistencia
        sum += self.agresividad + self.pase + self.habilidad
        return  sum // 9

    def getPosesionPelota(self):
        sum = self.marca + self.velocidad + self.resistencia + self.pase + self.habilidad
        return sum // 5