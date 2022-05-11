import random
from abc import abstractmethod

import names

class Jugador():


    def __init__(self):

        self.nombre = names.get_full_name(gender='male')
        self.edad = random.randint(18, 35)
        self.altura = random.randint(160, 190)
        self.peso = random.randint(40,80)
        self.precio = 0
        self.estadoFisico = "Bueno"
        self.posicion = " "
        #-----
        self.marca = 0
        self.potenciaTiro = 0
        self.velocidad = 0
        self.resistencia = 0
        self.agresividad = 0
        self.pase = 0
        self.manoAMano = 0
        self.tirosDeFalta = 0
        self.penales = 0
        self.gambeta = 0
        self.calidadTirosDeFalta = 0
        self.pase = 0
        self.inteligencia = 0
        self.habilidad = 0
        self.cabezaso = 0

    @abstractmethod
    def get_media(self):
        pass

    @abstractmethod
    def getPosesionPelota(self):
        pass

#---------------Getters And Setters
    def get_Marca(self):
        return self.marca

    def get_PotenciaTiro(self):
        return self.potenciaTiro

    def get_Velocidad(self):
        return self.velocidad

    def get_Resistencia(self):
        return self.resistencia

    def get_Agresividad(self):
        return self.agresividad

    def get_Pase(self):
        return self.pase

    def get_ManoAMano(self):
        return self.manoAMano

    def get_TirosDeFalta(self):
        return self.tirosDeFalta

    def get_Penales(self):
        return self.penales

    def get_Gambeta(self):
        return self.gambeta

    def get_CalidadTirosDeFalta(self):
        return self.calidadTirosDeFalta

    def get_Pase(self):
        return self.pase

    def get_Inteligencia(self):
        return self.inteligencia

    def get_Habilidad(self):
        return self.habilidad

    def get_Cabezaso(self):
        return self.cabezaso

    def get_Posicion(self):
        return self.posicion



