#Realizar un programa loteria

print("bienvenido al programa para adivinar la loteria")
#cambiar
numero_ganador = int(input("ingrese el numero ganador"))
#fijo
#numero_ganador = 8

bucle=True

while(bucle==True):
    a=int( input("ingrese un numero"))
    #abs es para devolver el valor "absoluto" de una cuenta
    diferencia= abs(numero_ganador - a)
    if(diferencia == 0 ):
        print("felicidades ganaste!!!!!!!!!!!")
        bucle==False
    elif(diferencia > 0 and diferencia < 20):
        print("estas cerca...")
    elif(diferencia > 20 and diferencia < 50):
        print("estas un poco lejos..")
    elif(diferencia > 50):
        print("estas muy lejos")