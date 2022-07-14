#include <stdio.h>
#include <stdlib.h>

//PRÉ-incremento ++x;

//PÓS-incremento x++;

//PRÉ-decremento --x;

//PÓS-decremento x--;

/*
Sintaxe:
for(variável; condição; incremento)
{
    comando;
}
Sintaxe para loop infinito:
for( ; ; )
{
    comando;
}
*/
int main()
{
    int a;
    printf("Descubra a tabuada do número que desejar: ");
    scanf("%d", &a);
    for (int i = 1; i <= 10; i++)//será executado até a condição ser atendida
    {
        printf("%ix = %i\n", i, a * i);
    }
    return 0;
}