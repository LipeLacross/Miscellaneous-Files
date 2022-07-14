#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
Sintaxe para concatenar:
strcat(<string_destino>, <string_origem>);
strncpy(<string_destino>, <string_origem>, <tamanho>);
*/
int main()
{
    char nome[15] = "micael";
    char sobrenome[15] = " preto";
    char profissao[15] = " corno vacilão";
    
    strcat(nome, " souza");// corno será adicionado para o nome de micael
    strcat(nome, sobrenome);
    strncat(nome, profissao, 6);
    
    printf("nome completo: %s\n", nome);
}