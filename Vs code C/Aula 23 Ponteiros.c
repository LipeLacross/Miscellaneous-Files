#include <stdio.h>
#include <stdlib.h>

/*
Sintaxe:
tipo *nome_ponteiro;
Onde temos:
tipo : é o tipo de dado da variável cujo endereço o ponteiro armazena.
*nome_ponteiro : O nome da variável ponteiro.
*/
int main()
{
    //valor é a variável que
    //será apontada pelo ponteiro
    int valor = 27;

    //declaração de variável ponteiro
    // para armazenar endereços de memória
    int *ptr;

    //atribuindo o endereço da variável valor ao ponteiro
    ptr = &valor; //&valor tem um endereço de memória // é preciso usar o &

    printf("Utilizando ponteiros\n\n");
    printf("Conteudo da variavel valor: %d\n", valor);
    printf("Endereço da variavel valor: %x \n", &valor);
    //%x para mostrar valores hexadecimais, todo endereço de memória é um hexadecimal
    printf("Conteudo da variavel ponteiro ptr: %x", ptr);

    return 0;
}
