#include <stdio.h>
#include <stdlib.h>

/*
Sintaxe:
while(condição)
{
    comando;
}
Sintaxe para loop:
while (1)// condição verdadeira gerando um loop infinito
{
    comando;
}
 */
int main()
{
    float x, z;
    x = z = 1;

    while (x != 0)//pode ser usado para char
    {
        printf("Insira o primeiro número: ");
        scanf("%f", &x);

        printf("Insira o segundo número: ");
        scanf("%f", &z);

        printf("Soma: %.2f\n", (x + z));
        printf("Subtração: %.2f\n", (x - z));
        printf("Multiplicação: %.2f\n", (x * z));
        printf("Divisão: %.2f\n", x / z);
    }
    return 0;
}