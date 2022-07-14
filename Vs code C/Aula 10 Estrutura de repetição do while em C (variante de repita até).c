#include <stdio.h>
#include <stdlib.h>

/*
Sintaxe:
do
{
    comando 1;
    comando 2;
} while (condição);

A diferença entre o comando while e o do…while é 
justamente o local onde a condição que controla o laço é testada.

No comando while a condição é testada antes do bloco de 
instruções, e caso a condição seja falsa a repetição não será executada.

No do…while o bloco de comandos é executado pelo menos 
uma vez de forma obrigatória, independente do resultado da expressão lógica.
*/
void limpar_entrada() {
char c;
while ((c = getchar()) != '\n' && c != EOF) {}
}

int main()
{
    float C, F;
    char resp;
    
    do
    {
        printf("Digite a temperatura em Celsius: ");
        scanf("%f", &C);
        F = 9.0 * C / 5.0 + 32.0;
        printf("Equivalente em Fahrenheit: %.1f\n", F);
        printf("Deseja repetir (s/n)? ");
        //limpar_entrada();
        scanf(" %c", &resp);
    } while (resp == 's');
    return 0;
}