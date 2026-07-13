import random
#generar un TA-TE-TI para que lo vea el usuario
def tablero():
    print("\n")
    print("|",tablero_lista[0] + " |" ,tablero_lista[1] + " | "+ tablero_lista[2] + " |")
    print("|",tablero_lista[3] + " |" ,tablero_lista[4] + " | "+ tablero_lista[5] + " |")
    print("|",tablero_lista[6] + " |" ,tablero_lista[7] + " | "+ tablero_lista[8] + " |")
    print("\n")

#Creamos una funcion para los turnos
def turnos():
    #llamos me forma globlar la variable ganar y tablero_lista
    global ganar,tablero_lista
    print("[[[[[[EMPIEZA EL JUEGO]]]]]]")
    #llama a la funcion tablero
    tablero()
    for i in range (5):
        print("Turno de jugador 1. X")
        #la variable valor toma el valor de X simulando la jugada del Jugador 1
        valor="X"
        #la funcion jugada tima un parametro valor
        jugada(valor)
        #llama a la funcion ganarfuncion
        ganarfuncion()
        #se arma la condicion para saber si alguien ya gano o si puede jugar el otro jugador y tambien para que las jugadas sea menor a 4
        if ganar !=True and i<4:
         for g in range (4):
            print("turno de jugador 2. O")
            #ahora el valor toma el valor de O para simular la jugada 2
            valor="O"
            jugada(valor)
            ganarfuncion()
            if ganar ==True:
              print("\nfelidades ganaste jugador 2")
              #pregunta si desea jugar de nuevo .
              pay2=input("\ndesea jugar de nuevo?(s/n)")
              if pay2=='s':
                    tablero_lista=["-","-","-",
               "-","-","-",
               "-","-","-",]
                    turnos()
              else:
                    exit()
            break
        elif ganar ==True:
            print("\nfelidades ganaste jugador 1")
            #ahora el jugador 1 gano y pregunta si desea jugar de nuevo.
            pay=input("\ndesea jugar de nuevo?(s/n)")
            if pay=='s':
                    tablero_lista=["-","-","-",
               "-","-","-",
               "-","-","-",]
                    turnos()
            else:
                    exit()
        else:
            #ahora nuestra 3er opcion es el empate, por eso el condicional anidado arriba de "menor a 4"
            print("tenemos un empate\n")
            pay3=input("\ndesea jugar de nuevo?(s/n)")
            if pay3=='s':
                tablero_lista=["-","-","-",
               "-","-","-",
               "-","-","-",]
                turnos()
            else:
                exit()
            
#aca se genero una version paralela al programa para simular la simulacion de jugador contra maquina. la maquina optara por
# movimientos alatoreos que no generan un gran desafio a vencer,pero asi se logro jugar contra la maquina.         
def turnos2():
    global ganar,tablero_lista
    print("[[[[[[EMPIEZA EL JUEGO]]]]]]")
    tablero()
    for i in range (5):
        print("Turno de jugador 1. X")
        valor="X"
        jugada(valor)
        ganarfuncion()
        if ganar !=True and i<4:
         for g in range (4):
            print("turno de jugador 2,la maquina. O")
            valor="O"
            jugadamaq(valor)
            ganarfuncion()
            if ganar ==True:
              print("\nfelidades ganaste jugador 2")
              pay2=input("\ndesea jugar de nuevo?(s/n)")
              if pay2=='s':
                    tablero_lista=["-","-","-",
               "-","-","-",
               "-","-","-",]
                    turnos2()
              else:
                    exit()
            break
        elif ganar ==True:
            print("\nfelidades ganaste jugador 1")
            pay=input("\ndesea jugar de nuevo?(s/n)")
            if pay=='s':
                    tablero_lista=["-","-","-",
               "-","-","-",
               "-","-","-",]
                    turnos2()
            else:
                    exit()
        else:
            print("tenemos un empate\n")
            pay3=input("\ndesea jugar de nuevo?(s/n)")
            if pay3=='s':
                tablero_lista=["-","-","-",
               "-","-","-",
               "-","-","-",]
                turnos2()
            else:
                exit()


#se define la funcion para que juegue la maquina.
def jugadamaq(valor):    
    puede_anotar=False
    while puede_anotar==False:
        #aca genera el movimiento alatoreo del uno al nueve, para luego restar su posicion y encajarlo en su tablero.
        donde_anota= random.randint(1,9)
        donde_anota -= 1
          #hace referencia al item de la lista "donde anota".
        if tablero_lista[donde_anota] == "-":
            puede_anotar= True
        else:
            print("no puede anotar")
    tablero_lista[donde_anota]= valor
    tablero()

#definimos una funcion que recibe como parametro la variable "valor".
def jugada(valor):
    
    puede_anotar=False
    #aqui tenemos un buble ciclo while para que se repita en caso de que se pueda anotar.
    while puede_anotar==False:
        donde_anota=int(input("donde desea anotar?,eliga la posicion del 1 al 9: "))
        donde_anota -= 1
          #hace referencia al item de la lista "donde anota"
        if tablero_lista[donde_anota] == "-":
            puede_anotar= True
        else:
            print("no puede anotar")
    tablero_lista[donde_anota]= valor
    tablero()   



def ganarfuncion():
    global ganar
    #condicion para ganar de forma horizontal
    #la logica que se pensó para tomar como valido y ganador es, que si la pocicion 0 de la lista es igual a la posicion 1 y asi para la 2.
    #independientemente del "valor" que toma dicha posicion, puede ser X o puede ser O y tambien debe ser diferente a "-".
    #siendo que nosotros le dimos la posicion inicial "-" solo devolvera true en caso de 3 similitudes.
    if (tablero_lista[0]==tablero_lista[1]==tablero_lista[2] !="-"):
        print("tenemos un ganador")
        ganar=True
    elif (tablero_lista[3]==tablero_lista[4]==tablero_lista[5] !="-"):
        print("tenemos un ganador")
        ganar=True
    elif  (tablero_lista[6]==tablero_lista[7]==tablero_lista[8] !="-"):
        print("tenemos un ganador")
        ganar=True
    #condicion para ganar de forma diagonal
    elif  (tablero_lista[0]==tablero_lista[4]==tablero_lista[8] !="-"):
        print("tenemos un ganador")
        ganar=True
    elif  (tablero_lista[6]==tablero_lista[4]==tablero_lista[2] !="-"):
        print("tenemos un ganador")
        ganar=True 
    #condicion para ganar de forma vertical
    elif  (tablero_lista[2]==tablero_lista[5]==tablero_lista[8] !="-"):
        print("tenemos un ganador")
        ganar=True
    elif  (tablero_lista[0]==tablero_lista[3]==tablero_lista[6] !="-"):
        print("tenemos un ganador")
        ganar=True  
    elif  (tablero_lista[1]==tablero_lista[4]==tablero_lista[7] !="-"):
        print("tenemos un ganador")
        ganar=True    
    else:
        ganar=False

#aca se crea la lista principal del programa, 
tablero_lista=["-","-","-",
               "-","-","-",
               "-","-","-",]
#variables de control booleanas.
ganar=False
v1=True
#ciclo principal del programa el mismo esta realizado con un while.
while v1==True:
    print("bienvenido al programa para jugar al tateti")
    print("presione 1 para jugar contra otro jugador ")
    print("presione 2 para jugar contra la maquina ")
    opcion=int(input("ingrese una opcion"))
    if opcion==1:
        tablero_lista=["-","-","-",
               "-","-","-",
               "-","-","-",]
        turnos()
    else:
        tablero_lista=["-","-","-",
               "-","-","-",
               "-","-","-",]
        turnos2()