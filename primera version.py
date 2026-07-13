#creamos el objeto llamado personaje
class personaje:
    #1nombre="Default"
    #1fuerza=0
    #1inteligencia=0
    #1defensa=0
    #1vida=0

    #definimos una funcion "def"+"init" para darle acceso a los atributos y metodos de la clase"personaje"
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        #cambiara el atributo que reciba 
        self.nombre=nombre
        self.fuerza=fuerza
        self.inteligencia=inteligencia
        self.defensa=defensa
        self.vida=vida
        #1ahora crearemos una fx para los atributos y como mostrarlos   
    def atributos(self):
        print(self.nombre,":" ,sep= "")
        print(".Fuerza",self.fuerza)
        print(".Inteligencia",self.inteligencia)
        print(".Defensa",self.defensa)
        print(".Vida",self.vida)
        #2crearemos una fx para la accion de subir nivel para ello necesitamos aclararle que atributos y las nuevas estadisticas  
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza+fuerza
        self.inteligencia = self.inteligencia+inteligencia
        self.defensa = self.defensa + defensa
        #3creamos fx para saber si aun sigue vivo nuestro pj esto debe ser una sentencia de repeticion infinita "boold"
    def esta_vivo(self):
        #comprobamos que este vivo con return,para devolver, del atributo vida y la devolucion self
        return self.vida>0
        #4creamos fx para morir
    def morir(self):
        self.vida =0
        print(self.nombre,"ah muerto")
        #5 calcularemos el daño que hace nuestro pj a un enemigo
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
        #6 fx para atacar lo cual deve contar el daño y la vida restantes
    def atacar(self, enemigo):
        daño = self.daño (enemigo)
        enemigo.vida= enemigo.vida-daño
        print(self.nombre, "ah realizado",daño,"puntos de daño a ",enemigo.nombre)
        #7comprobamos si esta vivo el enemigo
        if enemigo.esta_vivo():
            print("la vida de ",enemigo.nombre, "es",enemigo.vida )
        else:
            #7llamamos a la fx morir
            enemigo.morir()
#8HERENCIAS debemos definir la clase herencia y luego la clase padre
class guerrero(personaje):
        #8 sobreescribimos la funcion init
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        #8.1 deberiamos inicializar los atributos
        # personaje.__init__(self, nombre, fuerza, inteligencia, defensa, vida)
        #8.2 pero se puede hacer de otra forma con "super"
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        #8.2 con esto evitamos que a la hora de cambiar de "padre"osea "personaje" debamos hacerlo dentro del codigo tmb.
        #8incluimos a la espada
        self.espada = espada
        #9creamos una funcion para cambiar de arma
    def cambiar_arma(self):
        #9.1 debemos crear una variable para saber que opcion de arma eligió
        opcion_de_arma= int(input("elige un arma: (1) arma de madera, daño 8 (2) arma de hieroo, daño 10"))
        #armamos el daño
        if opcion_de_arma == 1:
            self.espada = 8
        elif opcion_de_arma == 2:
            self.espada = 10
        else:
            print("no ingreso arma correspondiente")
        #9.2 añadimos el atributo espada para que lo muestre en pantalla
    def atributos(self):
        super().atributos()
        print(".Espada",self.espada)
    def daño(self, enemigo):
         return self.fuerza * self.espada - enemigo.defensa
    #10nueva clase mago
class mago(personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    def atributos(self):
        super().atributos()
        print(".Libro",self.libro)
    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa
    #12 ahora crearemos funciones para la batalla
def combate(personaje_1,personaje_2):
    turno =0
    while personaje_2.esta_vivo() and personaje_1.esta_vivo():
        print("\nturno",turno)
        print(">>accion de: ",personaje_1.nombre,":", sep="")
        personaje_1.atacar(personaje_2)
        print(">>accion de: ",personaje_2.nombre,":", sep="")
        personaje_2.atacar(personaje_1)
        turno=turno + 1
    if personaje_1.esta_vivo():
        print("\nah ganado",personaje_1.nombre)
    elif personaje_2.esta_vivo():
        print("\nah ganado",personaje_2.nombre)
    else:
        print("\nempate")
#llamamos al objeto y le designamos una variable
#mi_personaje = personaje("german",8,5,3,100)

#5creamos al enemigo
#mi_enemigo = personaje("orco",3,3,1,6)
#podriamos modificar los atributos del objeto antes de mostrarlos con la sintaxis.- mi_personaje.nombre = "german" -.

#1print("el nombre del personaje es: ",mi_personaje.nombre)
#1print("la fuerza es: ",mi_personaje.fuerza)
#1print("la inteligencia es: ",mi_personaje.inteligencia)
#1print("la defensa es: ",mi_personaje.defensa)
#1print("la vida es: ",mi_personaje.vida)
#llamamos ahora a la fx a traves de la variable
#mi_personaje.atributos()
#haremos la prueba para sumar estadisticas a nuestros atributos

#2 syntaxis mipersonaje.subir_nivel (1,2,0)
#mi_personaje.subir_nivel (1,2,0)
#2 syntaxis mi_personaje.atributos()
#mi_personaje.atributos()

#3 comprobamos si estamos vivos debe devolver "true"
#print(mi_personaje.esta_vivo())

#4 ejecutamos morir
#mi_personaje.morir()
#mi_personaje.atributos()
#mi_enemigo.atributos()

#5 ejecutamos el daño
#print(mi_personaje.daño(mi_enemigo))

#6 ejecutamos el ataque
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.atributos()

#8 HERENCIAS "sumaremos un atributo nuevo a nuestra herencia"
Aragon = guerrero("Aragon",18,15,13,10000,5)
Aragon.cambiar_arma()
Aragon.atributos()
#print(Aragon.espada)

#10nueva clase mago
#saruman =mago("saruman",7,25,5,110,70)
#saruman.atributos()

#11 probamos atacar entre los personajes creados
#saruman.atacar(mi_personaje)
#mi_personaje.atributos()

#12combate
#personaje_1= guerrero("gimbli",40,20,8,2000,4)
#personaje_1.atributos()
personaje_2= mago("saruman",10,30,5,5000,18)
personaje_2.atributos()
combate(Aragon,personaje_2)