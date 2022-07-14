#include <stdio.h>
#include <stdlib.h>

int main(void)
/*
Sintaxe:
Condição ? verdadeiro : falso

Seria o equivalente a usar if:
if (<variável1> <operação> <variável2>)
{
    comando1;
}
    else
    {
        comando2;
    }

*/
{
    int numero;

    printf("Digite um numero: ");
    scanf("%d", &numero);

    //numero >= 0 ? numero++ : numero--;
    numero >= 0 ? printf("é maior ou igual a zero") : printf("é menor que zero");
    //além de de fazer operações pode-se usar comandos
    printf("\nO valor do número é: %d", numero);

    return (0);
}