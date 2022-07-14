#include <stdio.h>
#include <stdlib.h>
#include <string.h> //necessário para strtok;

int main()
{

    char texto1[50] = "Fulano de Tal,Rua X,123,Centro,Cidade Y";
    char *t;

    //A função strtok() permite dividir uma string em partes.
    t = strtok(texto1, ",");
    //vai parar na vírgula

    while (texto1 != NULL)
    {
        printf("%s\n", t);
        t = strtok(NULL, ",");
        //NULL vai limpar a string anterior e continuar
    }

    return 0;
}