from Game.Eventos.Procesar import jugar_partido
import operator
import collections

def fase_Grupos(Equipo1,Equipo2,Equipo3,Equipo4):
    PtjeE1=0
    PtjeE2=0
    PtjeE3=0
    PtjeE4=0

    tupla = jugar_partido(Equipo1, Equipo2)

    if tupla[0] > tupla[1]:
        PtjeE1 += 3
    elif tupla[1] > tupla[0]:
        PtjeE2 += 3
    else:
        PtjeE1 += 1
        PtjeE2 += 1

    tupla = jugar_partido(Equipo1, Equipo3)

    if tupla[0] > tupla[1]:
        PtjeE1 += 3
    elif tupla[1] > tupla[0]:
        PtjeE3 += 3
    else:
        PtjeE1 += 1
        PtjeE3 += 1

    tupla = jugar_partido(Equipo1, Equipo4)
    if tupla[0] > tupla[1]:
        PtjeE1 += 3
    elif tupla[1] > tupla[0]:
        PtjeE4 += 3
    else:
        PtjeE1 += 1
        PtjeE4 += 1

    tupla = jugar_partido(Equipo2, Equipo3)
    if tupla[0] > tupla[1]:
        PtjeE2 += 3
    elif tupla[1] > tupla[0]:
        PtjeE3 += 3
    else:
        PtjeE2 += 1
        PtjeE3 += 1

    tupla = jugar_partido(Equipo2, Equipo4)
    if tupla[0] > tupla[1]:
        PtjeE2 += 3
    elif tupla[1] > tupla[0]:
        PtjeE4 += 3
    else:
        PtjeE2 += 1
        PtjeE4 += 1

    tupla = jugar_partido(Equipo3, Equipo4)
    if tupla[0] > tupla[1]:
        PtjeE3 += 3
    elif tupla[1] > tupla[0]:
        PtjeE4 += 3
    else:
        PtjeE3 += 1
        PtjeE4 += 1

    max1 = -1
    max2 = -1
    Eq1 = Equipo4
    print(PtjeE1, PtjeE2, PtjeE3, PtjeE4)
    if PtjeE1 > max1:
        Eq1 = Equipo1
        max1 = PtjeE1
    elif PtjeE1 > max2:
        Eq2 = Equipo1
        max2 = PtjeE1
    if PtjeE2 > max1:
        auxPtje = max1
        auxEq = Eq1
        Eq1 =  Equipo2
        max1 = PtjeE2
        Eq2 = auxEq
        max2 = auxPtje
    elif PtjeE2 >= max2:
        Eq2 = Equipo2
        max2 = PtjeE2
    if PtjeE3 > max1:
        auxPtje = max1
        auxEq = Eq1
        Eq1 =  Equipo3
        max1 = PtjeE3
        Eq2 = auxEq
        max2 = auxPtje
    elif PtjeE3 >= max2:
        Eq2 = Equipo3
        max2 = PtjeE3
    if PtjeE4 > max1:
        aux = Eq1
        Eq1 = Equipo4
        Eq2 = aux
    elif PtjeE4 >= max2:
        Eq2 = Equipo4

    return Eq1,Eq2
    #print(Eq1.get_Nombre())
    #print(Eq2.get_Nombre())

def fase_Grupos2(Equipo1,Equipo2,Equipo3,Equipo4):
    dictE = {Equipo1:0,Equipo2:0, Equipo3:0,Equipo4:0}

    tupla = jugar_partido(Equipo1, Equipo2)

    if tupla[0] > tupla[1]:
        dictE.update({Equipo1: dictE[Equipo1]+3})
    elif tupla[1] > tupla[0]:
        dictE.update({Equipo2: dictE[Equipo2]+3})
    else:
        dictE.update({Equipo1: dictE[Equipo1]+1})
        dictE.update({Equipo2: dictE[Equipo2]+1})

    tupla = jugar_partido(Equipo1, Equipo3)

    if tupla[0] > tupla[1]:
        dictE.update({Equipo1: dictE[Equipo1]+3})
    elif tupla[1] > tupla[0]:
        dictE.update({Equipo3: dictE[Equipo3]+3})
    else:
        dictE.update({Equipo1: dictE[Equipo1] + 1})
        dictE.update({Equipo3: dictE[Equipo3] + 1})

    tupla = jugar_partido(Equipo1, Equipo4)
    if tupla[0] > tupla[1]:
        dictE.update({Equipo1: dictE[Equipo1] + 3})
    elif tupla[1] > tupla[0]:
        dictE.update({Equipo4: dictE[Equipo4] + 3})
    else:
        dictE.update({Equipo1: dictE[Equipo1] + 1})
        dictE.update({Equipo4: dictE[Equipo4] + 1})

    tupla = jugar_partido(Equipo2, Equipo3)
    if tupla[0] > tupla[1]:
        dictE.update({Equipo2: dictE[Equipo2] + 3})
    elif tupla[1] > tupla[0]:
        dictE.update({Equipo3: dictE[Equipo3] + 3})
    else:
        dictE.update({Equipo2: dictE[Equipo2] + 1})
        dictE.update({Equipo3: dictE[Equipo3] + 1})

    tupla = jugar_partido(Equipo2, Equipo4)
    if tupla[0] > tupla[1]:
        dictE.update({Equipo2: dictE[Equipo2] + 3})
    elif tupla[1] > tupla[0]:
        dictE.update({Equipo4: dictE[Equipo4] + 3})
    else:
        dictE.update({Equipo2: dictE[Equipo2] + 1})
        dictE.update({Equipo4: dictE[Equipo4] + 1})

    tupla = jugar_partido(Equipo3, Equipo4)
    if tupla[0] > tupla[1]:
        dictE.update({Equipo3: dictE[Equipo3] + 3})
    elif tupla[1] > tupla[0]:
        dictE.update({Equipo4: dictE[Equipo4] + 3})
    else:
        dictE.update({Equipo3: dictE[Equipo3] + 1})
        dictE.update({Equipo4: dictE[Equipo4] + 1})

    print(dictE)
    valores_ord = dict(sorted(dictE.items(), reverse=True))
    valores_ord = collections.OrderedDict(sorted(dict.items()))
    print(valores_ord)
