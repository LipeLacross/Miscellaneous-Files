#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
Sintaxe para saber o tamanho de uma string:
<nome_da_variável do tipo inteiro> = strlen(<nome_da_string>);
*/
int main()
{
    char nome[] = "micael corno";
    int tamanho;

    tamanho = strlen(nome);

    printf("Quantidade de caracteres: %d\n", tamanho);
    //ou
    printf("Quantidade de caracteres: %d", strlen(nome));

    return 0;
}