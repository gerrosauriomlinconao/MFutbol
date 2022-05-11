import random

from Jugadores.Arquero import Arquero
from Jugadores.Defensa import Defensor
from Jugadores.Delantero import Delantero
from Jugadores.Volante import Volante

if __name__ == '__main__':
    val1 = random.randint(1,9)
    val2 = random.randint(1,9)
    val3 = random.randint(1,9)
    val4 = random.randint(1,9)
    print(val1)
    print(val2)
    print(val3)
    print(val4)
    print(".....")
    max1 = 0
    max2 = -1
    Eq1 = ""
    Eq2 = ""
    if val1 > max1:
        Eq1 = "Equipo1"
        max1 = val1
    elif val1 > max2:
        Eq2 = "Equipo1"
        max2 = val1
    if val2 > max1:
        Eq1 = "Equipo2"
        max1 = val2
    if val2 >= max2:
        Eq2 = "Equipo2"
        max2 = val2
    if val3 > max1:
        Eq1 = "Equipo3"
        max1 = val3
    if val3 >= max2:
        Eq2 = "Equipo3"
        max2 = val3
    if val3 > max1:
        Eq1 = "Equipo3"
        max1 = val3
    if val4 >= max2:
        Eq2 = "Equipo4"
        max2 = val4

    print(Eq1)
    print(Eq2)

