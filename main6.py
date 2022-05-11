from Campeonatos.Copa import fase_Grupos, fase_Grupos2
from Equipo.Equipo import Equipo
from Game.Eventos.Procesar import realizar_pase, delantero_definir, definir_posesion, jugar_partido

if __name__ == '__main__':
    Equipo1 = Equipo()
    Equipo2 = Equipo()
    Equipo3 = Equipo()
    Equipo4 = Equipo()
    print(Equipo1.nombre)
    print(Equipo2.nombre)
    print(Equipo3.nombre)
    print(Equipo4.nombre)

    tupla = fase_Grupos(Equipo1,Equipo2,Equipo3,Equipo4)
    g11 = tupla[0].get_Nombre()
    g12 = tupla[1].get_Nombre()
    print(g11)
    print(g12)
