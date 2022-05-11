import names

from Jugadores.Arquero import Arquero
from Jugadores.Defensa import Defensor
from Jugadores.Delantero import Delantero
from Jugadores.Jugador import Jugador
from Jugadores.Volante import Volante


class Equipo():

    def __init__(self):
        self.nombre = names.get_full_name(gender='male')
        self.lista_jugadores = []
        self.arquero = Arquero()
        self.lista_jugadores.append(self.arquero)
        for i in range(1,5):
            defensor = Defensor()
            volante = Volante()
            self.lista_jugadores.append(defensor)
            self.lista_jugadores.append(volante)

        delantero1 = Delantero()
        delantero2 = Delantero()
        self.lista_jugadores.append(delantero1)
        self.lista_jugadores.append(delantero2)

    def get_Nombre(self):
        return self.nombre

    def get_Posesion_Total(self):
        sum = 0
        for jugador in self.lista_jugadores:
            sum += jugador.getPosesionPelota()
        return sum

    def get_Jugadores(self):
        return self.lista_jugadores

    def get_Arqueros(self):
        return self.lista_jugadores[0:1]
    def get_Defensores(self):
        return self.lista_jugadores[1:5]
    def get_Volantes(self):
        return self.lista_jugadores[5:9]
    def get_Delantero(self):
        return self.lista_jugadores[9:12]


    def get_Potencia_Delanteros(self):
        sum = 0

        for jug in self.get_Delantero():
            sum += jug.get_PotenciaTiro() + jug.get_ManoAMano() + jug.get_Cabezaso() + jug.get_Agresividad() + jug.get_CalidadTirosDeFalta()

        return (sum // 2)

    def get_Potencia_Defensa(self):
        sum = 0
        for jug in self.get_Defensores():
            sum += jug.get_Marca() + jug.get_Velocidad() + jug.get_Agresividad()

        sum2 = 0
        for arq in self.get_Arqueros():
            sum2 += arq.get_ManoAMano() + arq.get_TirosDeFalta() + arq.get_Penales()

        return ((sum + sum2)// 4)
