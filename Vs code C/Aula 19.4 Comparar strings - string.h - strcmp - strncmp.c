#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
Sintaxe para comparar strings com base na tabela ASCII:
variável do tipo inteiro = strcmp(<string1>, <string2>);
*/
int main()
{
    char nome[] = "corno do micael";
    char nome2[] = "corno do cimael";
    int comparacao;
    int minicomparacao;

    comparacao = strcmp(nome, nome2);
    minicomparacao = strncmp(nome, nome2, 5);

    printf("comparando os nomes: %i\n", comparacao);
    //ou
    printf("comparando os nomes: %i\n", strcmp(nome, nome2));
    printf("comparando os nomes: %i\n", minicomparacao);// dá zero pq são iguais

    /*
    Possíveis valores de retorno:
    0: conteúdo das strings são iguais
    < 0: conteúdo da string1 é menor do que string2
    > 0: conteúdo da string1 é maior do que string2
    */
    return 0;
}