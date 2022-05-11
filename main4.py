from Equipo.Equipo import Equipo
from Game.Eventos.Procesar import realizar_pase, delantero_definir, definir_posesion, jugar_partido

if __name__ == '__main__':


    equipo1 = Equipo()
    equipo2 = Equipo()
    equipo3 = Equipo()
    equipo4 = Equipo()
    print(equipo1.nombre)
    print(equipo2.nombre)
    print(equipo3.nombre)
    print(equipo4.nombre)


    print(jugar_partido(equipo1,equipo2))
    print(jugar_partido(equipo1, equipo3))
    print(jugar_partido(equipo1, equipo4))
    print("++++++")
    print(jugar_partido(equipo2, equipo3))
    print(jugar_partido(equipo2, equipo4))
    print("++++++")
    print(jugar_partido(equipo3, equipo4))


