from Equipo.Equipo import Equipo
from Game.Eventos.Procesar import realizar_pase

if __name__ == '__main__':


    equipo1 = Equipo()
    print(equipo1.nombre)
    #for j in equipo1.get_Defensores():
       # print(j.get_Pase())

    print("---------------")
    cant = 0
    for i in range (0,20):
        if realizar_pase(equipo1.get_Defensores()) and realizar_pase(equipo1.get_Volantes()) and realizar_pase(equipo1.get_Delantero()):
            cant += 1
    print(cant)
     #print(realizar_pase(equipo1.get_Defensores()))
     #print(realizar_pase(equipo1.get_Volantes()))
     #print(realizar_pase(equipo1.get_Delantero()))
     #print(" ---- ")



  #  print(equipo1.get_Posesion_Total())
   # print(equipo2.get_Posesion_Total())

