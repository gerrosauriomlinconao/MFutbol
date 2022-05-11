
import numpy as np

def realizar_pase(listaJug):
    sum = 0
    for jug in listaJug:
        sum += jug.get_Pase()

    prom = sum//4 /100  #si por ejemplo el promedio es 75 necesito 0.75 para la ponderación
    val = [True, False]
    sRandom = np.random.choice(val, 1, p=[prom, 1-prom]) #la suma de valores de la ponderación debe ser = 1
    return sRandom[0]


def delantero_definir(Equipo1, Equipo2):
    ponderacion = (Equipo1.get_Potencia_Delanteros() - Equipo2.get_Potencia_Defensa())/100
    val = [True, False]
    sRandom = np.random.choice(val, 1, p=[ponderacion, 1 - ponderacion])  # la suma de valores de la ponderación debe ser = 1
    return sRandom[0]


def definir_posesion(Equipo1,Equipo2):
    return realizar_pase(Equipo1.get_Defensores()) and realizar_pase(Equipo1.get_Volantes()) and delantero_definir(Equipo1,Equipo2)

def jugar_partido(Equipo1,Equipo2):
    goles1 = 0
    goles2 = 0
    for i in range(0,10):
        if definir_posesion(Equipo1,Equipo2):
            goles1 += 1
        if definir_posesion(Equipo1,Equipo2):
            goles2 += 1

    return goles1,goles2



#-----------------

#def posesion_pelota(EquipoA,EquipoB):
#    print(EquipoA.get_Posesion_Total())
#    print(EquipoA.get_Posesion_Total() // 10)
#    print(EquipoB.get_Posesion_Total() // 10)


#si posesion de pelota E1 es mayor posesion de pelota E2 Y potencia ataque e1 > potencia ataque equipo 2 => gol
#si potencia ataque E1 - potencia defensa equipo 2 > 0 => gol
#calidadTirosDeFalta + potenciaTiro > E2 = gol
#velocidad + resistencia + habilidad - marcaE2 - velocidadE2 - resistenciaE2 = gol
#calidadTirosDeFalta + inteligencia + cabezaso + agresividad - agresividadE2 - marcaE2 - inteligenciaE2 - agilidad > 0 => gol

#--------------------------


