#include <stdio.h>
#include <stdlib.h>

/*A função utilizada dessa forma é denominada função com passagem por referência. 
Nesse tipo de função, os argumentos passam os endereços de memória para os parâmetros declarados na função. 
Sendo assim, os parâmetros que recebem os valores passados obrigatoriamente tem que ser ponteiros 
já que irão receber um endereço de memória.
*/

//função que soma 10 ao valor recebido
void soma10(int x)
{
    x = x + 10;
    printf("Valor de x apos a soma = %d \n", x);
    return;
}
void soma10ponteiro(int *x)//para a função com void funfar usa-se ponteiro
{
    *x = *x + 10;
    printf("Valor de x apos a soma = %d \n", *x);
    return;
}
int main()
{
    int numero;
    printf("Digite um numero: ");
    scanf("%d", &numero);

    printf("O numero digitado foi: %d \n", numero);

    soma10(numero); //chamada da função
    printf("Agora o numero vale: %d \n", numero);

    soma10ponteiro(&numero); //chamada da função com ponteiro como parâmetro
    printf("Agora o numero vale: %d \n", numero);

    return 0;
}