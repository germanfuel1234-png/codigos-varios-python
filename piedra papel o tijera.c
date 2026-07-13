#include <stdio.h>
#include <stdlib.h>
//define es para declarar true y false
#define FALSE 0
#define TRUE 1
//variables de control

int main(){
    //declaro variables
    int modo,control,jugada1,jugada2,victoria1,victoria2,numero,programa;
    char jugada3;
    //primer menu para ver que juega el usuario
    programa=1;
    while(programa==1){
    printf("bienvenido al piedra papel o tijera\n");
    printf("elija la opcion de juego \n");
    printf("1- j vs j\n");
    printf("2- j vs M\n");
    printf("3- salir.\n");
    scanf("%i",&modo);
    //guardo en mi variable la opcion del usuario
    victoria2=0;
    victoria1=0;
    //modo jugador vs jugador
    if (modo==1){
        printf("usted elijio el modo de jugador vs jugador\n");
        control=1;
        while(control==1){
            //jugada del primer jugador
            printf("turno del jugador UNO\n");
            printf("1-papel\n");
            printf("2-piedra\n");
            printf("3-tijera\n");
            scanf("%i",&jugada1);
            printf("turno del jugador DOS\n");
            printf("1-papel\n");
            printf("2-piedra\n");
            printf("3-tijera\n");
            scanf("%i",&jugada2);
            //caso empate
            if(jugada1 == jugada2){
                printf("empate");}
                else if((jugada1==1 && jugada2==2|| jugada1==2 &&jugada2==3 || jugada1==3 &&jugada2==1)){
                    printf("gana jugador 1\n\n");
                    //expresion logica para el control de el tanteador
                    victoria1=victoria1+1;
                }
                    else{
                        printf("gana jugador 2\n\n");
                    victoria2=victoria2+1;
                    }
            printf("victorias del jugador 1 tablero:  %i \n victorias del jugadoar 2 tablero%i \n",victoria1,victoria2);
            if((victoria2>2) || (victoria1>2)){
                control=2;
                
            }
        }
        
    }
    else if (modo==2){
        control=1;
        while(control==1){
        printf("Turno del jugador UNO\n");
        printf("1- Papel\n");
        printf("2- Piedra\n");
        printf("3- Tijera\n");
        scanf("%i", &jugada1);
        //numero random
        numero = rand() % 3 + 1;
        printf("La máquina eligio: %i\n", numero);
        if (jugada1 == numero) {
            printf("Empate\n");
        } else if ((jugada1 == 1 && numero == 2) || (jugada1 == 2 && numero == 3) || (jugada1 == 3 && numero == 1)) {
            printf("Gana el jugador\n\n");
            victoria1++;
        } else {
            printf("Gana la maquina\n\n");
            victoria2++;
        }
        
        printf("Victorias del jugador 1: %i\nVictorias de la máquina: %i\n", victoria1, victoria2);
        if((victoria2>2) || (victoria1>2)){
                control=2;
            }
        }
    }
    else{
    printf("saliste del programa");
        
    }
    
    printf("desea volver a jugar (s/n)");
    scanf(" %c", &jugada3);
        if(jugada3=='s'){
            programa=1;}
        else{
            programa=2;
        }
        
    }
   return 0;
        
    }