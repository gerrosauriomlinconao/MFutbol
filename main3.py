from Equipo.Equipo import Equipo
from Game.Eventos.Procesar import realizar_pase, delantero_definir

if __name__ == '__main__':


    equipo1 = Equipo()
    equipo2 = Equipo()
    print(equipo1.nombre)
    print(equipo2.nombre)
    G1 = 0
    G2 = 0
    empate = 0
    for i in range (0,10):
        cantGolesEquipo1 = 0
        cantGolesEquipo2 = 0

        for i in range(0,10):

            if (delantero_definir(equipo1, equipo2)):
                cantGolesEquipo1+=1
            if (delantero_definir(equipo2, equipo1)):
                cantGolesEquipo2 += 1

        if cantGolesEquipo1 > cantGolesEquipo2:
            G1 += 1
        elif cantGolesEquipo2 > cantGolesEquipo1:
            G2 += 1
        else:
            empate += 1
        print("+++++  ++++++")
        print("Goles Equipo 1: ", cantGolesEquipo1)
        print("Goles Equipo 2: ", cantGolesEquipo2)
        print("+++++  ++++++")


    print( "gana 1: ", G1)
    print("gana 2: ", G2)
    print("empate: ", empate)
    print("-----------")


