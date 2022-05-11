from Campeonatos.Copa import fase_Grupos, fase_Grupos2
from Equipo.Equipo import Equipo
from Game.Eventos.Procesar import realizar_pase, delantero_definir, definir_posesion, jugar_partido

if __name__ == '__main__':
    Equipo1 = Equipo()
    Equipo2 = Equipo()
    Equipo3 = Equipo()
    Equipo4 = Equipo()
    Equipo5 = Equipo()
    Equipo6 = Equipo()
    Equipo7 = Equipo()
    Equipo8 = Equipo()
    Equipo9 = Equipo()
    Equipo10 = Equipo()
    Equipo11 = Equipo()
    Equipo12= Equipo()
    Equipo13= Equipo()
    Equipo14 = Equipo()
    Equipo15 = Equipo()
    Equipo16 = Equipo()


    print('Fase de grupos.........................')
    print("-----grupo 1----------")
    tupla = fase_Grupos(Equipo1,Equipo2,Equipo3,Equipo4)
    print(Equipo1.get_Nombre())
    print(Equipo2.get_Nombre())
    print(Equipo3.get_Nombre())
    print(Equipo4.get_Nombre())
    print("++++++++")
    g11 = tupla[0]
    g12 = tupla[1]
    print(g11.get_Nombre())
    print(g12.get_Nombre())
    print("-----fin grupo 1----------")
    print("-----grupo 2----------")
    print(Equipo5.get_Nombre())
    print(Equipo6.get_Nombre())
    print(Equipo7.get_Nombre())
    print(Equipo8.get_Nombre())
    print("++++++++")
    tupla = fase_Grupos(Equipo5,Equipo6,Equipo7,Equipo8)
    g21 = tupla[0]
    g22 = tupla[1]
    print(g21.get_Nombre())
    print(g22.get_Nombre())
    print("-----fin grupo 2----------")
    print("-----grupo 3----------")
    print(Equipo9.get_Nombre())
    print(Equipo10.get_Nombre())
    print(Equipo11.get_Nombre())
    print(Equipo12.get_Nombre())
    print("++++++++")
    tupla = fase_Grupos(Equipo9,Equipo10,Equipo11,Equipo12)
    g31 = tupla[0]
    g32 = tupla[1]
    print(g31.get_Nombre())
    print(g32.get_Nombre())
    print("-----fin grupo 3----------")
    print("-----grupo 4----------")
    print(Equipo13.get_Nombre())
    print(Equipo14.get_Nombre())
    print(Equipo15.get_Nombre())
    print(Equipo16.get_Nombre())
    print("++++++++")
    tupla = fase_Grupos(Equipo13, Equipo14, Equipo15, Equipo16)
    g41 = tupla[0]
    g42 = tupla[1]
    print(g41.get_Nombre())
    print(g42.get_Nombre())
    print("-----fin grupo 4----------")
    print("-----Cuartos----------")
    tupla = jugar_partido(g11, g22)
    print(g11.get_Nombre(), tupla[0])
    print(g22.get_Nombre() , tupla[1])
    print(tupla)
    if tupla[0] > tupla[1]:
        GC1 = g11
    else:
        GC1 = g22
    print("Ganador Cuartos 1:", GC1.get_Nombre())
    tupla = jugar_partido(g12, g21)
    print(g12.get_Nombre(), tupla[0])
    print(g21.get_Nombre(), tupla[1])
    print(tupla)
    if tupla[0] > tupla[1]:
        GC2 = g11
    else:
        GC2 = g22
    print("Ganador Cuartos 2:", GC2.get_Nombre())
    tupla = jugar_partido(g31, g42)
    print(g31.get_Nombre(), tupla[0])
    print(g42.get_Nombre(), tupla[1])
    print(tupla)
    if tupla[0] > tupla[1]:
        GC3 = g31
    else:
        GC3 = g42
    print("Ganador Cuartos 3:", GC3.get_Nombre())
    tupla = jugar_partido(g41, g32)
    print(g41.get_Nombre(), tupla[0])
    print(g32.get_Nombre(), tupla[1])
    print(tupla)
    if tupla[0] > tupla[1]:
        GC4 = g41
    else:
        GC4 = g32
    print("Ganador Cuartos 4:", GC4.get_Nombre())
    print("Semifinales: ")
    tupla = jugar_partido(GC1, GC2)
    print(GC1.get_Nombre(), tupla[0])
    print(GC2.get_Nombre(), tupla[1])
    print(tupla)
    if tupla[0] > tupla[1]:
        GS1 = GC1
    else:
        GS1 = GC2
    print("Ganador Semifinales 1:", GS1.get_Nombre())
    tupla = jugar_partido(GC3, GC4)
    print(GC3.get_Nombre(), tupla[0])
    print(GC4.get_Nombre(), tupla[1])
    print(tupla)
    if tupla[0] > tupla[1]:
        GS2 = GC3
    else:
        GS2 = GC4
    print("Ganador Semifinales 2:", GS2.get_Nombre())
    print("Final!")
    tupla = jugar_partido(GS1, GS2)
    print(GS1.get_Nombre(), tupla[0])
    print(GS2.get_Nombre(), tupla[1])
    print(tupla)
    if tupla[0] > tupla[1]:
        C = GS1
    else:
        C = GS2
    print("Campeon :", C.get_Nombre())




