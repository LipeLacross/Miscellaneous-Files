#include <stdio.h>
#include <stdlib.h>

/*
Sintaxe:
if (condição1) {
comando1
comando2
}
else if (condição2) {
comando3
comando4
}
else {
comando5
comando6
}
*/
int main()
{
    int hora;

    printf("Digite uma hora do dia: ");
    scanf("%d", &hora);

    if (hora < 12) //significa "se", se a condição for verdadeira o comando será executado
    {
        printf("Bom dia!\n");
    }
    //else if pode ser usado a vontade
    else if (hora > 12 && hora < 18) //condição extra a ser verificada
    {
        printf("Boa tarde!\n");
    }
    else if (hora > 18 && hora < 24) //condição extra a ser verificada
    {
        printf("Boa noite!\n");
    }
    else //significa "se não", será executado se nenhuma condição anterior for atendida
    {
        printf("Error");
    }

    return 0;
}