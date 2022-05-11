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

    puntosE1 = 0
    puntosE2 = 0
    puntosE3 = 0
    puntosE4 = 0
    tupla = jugar_partido(equipo1,equipo2)
    print("Equipo1 vs Equipo2", tupla)
    if tupla[0] > tupla[1]:
        puntosE1 += 3
    elif tupla[1] > tupla[0]:
        puntosE2 += 3
    else:
        puntosE1 += 1
        puntosE2 += 1

    tupla= jugar_partido(equipo1, equipo3)
    print("Equipo1 vs Equipo3", tupla)

    if tupla[0] > tupla[1]:
        puntosE1 += 3
    elif tupla[1] > tupla[0]:
        puntosE3 += 3
    else:
        puntosE1 += 1
        puntosE3 += 1

    tupla = jugar_partido(equipo1, equipo4)
    print("Equipo1 vs Equipo4", tupla)

    if tupla[0] > tupla[1]:
        puntosE1 += 3
    elif tupla[1] > tupla[0]:
        puntosE4 += 3
    else:
        puntosE1 += 1
        puntosE4 += 1

    print("++++++")
    tupla = jugar_partido(equipo2, equipo3)
    print("Equipo2 vs Equipo4", tupla)
    if tupla[0] > tupla[1]:
        puntosE2 += 3
    elif tupla[1] > tupla[0]:
        puntosE3 += 3
    else:
        puntosE2 += 1
        puntosE3 += 1

    tupla = jugar_partido(equipo2, equipo4)
    print("Equipo2 vs Equipo4", tupla)
    if tupla[0] > tupla[1]:
        puntosE2 += 3
    elif tupla[1] > tupla[0]:
        puntosE4 += 3
    else:
        puntosE2 += 1
        puntosE4 += 1

    print("++++++")
    tupla = jugar_partido(equipo3, equipo4)
    print("Equipo3 vs Equipo4", tupla)
    if tupla[0] > tupla[1]:
        puntosE3 += 3
    elif tupla[1] > tupla[0]:
        puntosE4 += 3
    else:
        puntosE3 += 1
        puntosE4 += 1


    print("Puntos E1: ", puntosE1)
    print("Puntos E2: ", puntosE2)
    print("Puntos E3: ", puntosE3)
    print("Puntos E4: ", puntosE4)


