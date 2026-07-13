#importamos la libreria random para calcular el numero de ticek de forma aleatoria
import random 
import json
#creamos una funcion para el alta de ticket       
def alta_ticket():
    print("\ningrese los datos para generar un nuevo ticket\n")
    nombre = input("ingrese su nombre ")
    sector = input("ingrese su sector ")
    asunto = input("ingrese su asunto ")
    problema = input("ingrese su problema")
    #iniciamos nuestro diccionario "datos"
    datos = {
    "nombre": nombre,
    "sector": sector,
    "asunto": asunto,
    "problema":problema,
    
            }
    #genera numero random
    numeroazar=random.randint(1000, 9999)
    #en base a nuestra vadiable "numeroazar" ,generamos el nombre del archivo.
    nombrejson=f"{numeroazar}.json" 
    # Crear y escribir en un archivo JSON
    with open(nombrejson, 'w') as archivoj:
        json.dump(datos, archivoj, indent=4)
    #imprime en pantalla de forma ordenada el diccionario previamenta cargador por el usuario
    print(datos)
    print(f"guarde su numero de ticket {numeroazar}")

def ver_ticket():
    numero_ticket=int(input("ingrese su numero de ticket"))
    nombre_json_ticket=f"{numero_ticket}.json"
    print(f"datos cargados desde json con el numero de ticket: {numero_ticket}")
    with open(nombre_json_ticket,'r') as lecturaj:
        data= json.load(lecturaj) 
        print(json.dumps(data,indent=4))      

#variable de control
n1=True

while n1 ==True :
    print("\nopcion 1: generar tiket")
    print("opcion 2: ver tiket")
    print("opcion 3: salir del programa")
    opcion = int(input("Ingresar una opcion: "))
    #condicional de decision.
    if opcion == 1:
        #variable de control numero 2
        n2='s'
        while n2=='s':
         #llamamos a la funcion alta_ticket
         alta_ticket()

         n2=input("desea generar otro ticket (s/n)")
         if n2=='s':
            n2=='s'
         else:
            n1=True
    if opcion == 2:
        ver_ticket()
        ticket2 = input("\ndesea leer otro ticket? (s/n)")
        if ticket2 == 's':
         ver_ticket()
        else:
         n1=True
    if opcion == 3:
        n1=False
    else:
        print("opcion incorrecta")
        n1=True