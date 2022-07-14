#include <stdio.h>
#include <stdlib.h>
#include <string.h>//para funfar strcpy

/*
Sintaxe para copiar dados de uma string para outra:
strcpy(<string_destino>, <string_origem>);
strncpy(<string_destino>, <string_origem>, <tamanho>);
*/
int main()
{
    char nome[15];
    char nome2[15];
    char nome3[15];
    
    strcpy(nome, "micael corno");
    strcpy(nome2, nome);//micael corno vai para nome2
    strncpy(nome3, nome, 6);//vai trazer os 6 primeiros caracteres para nome3
    
    printf("nome = %s\n", nome);
    printf("nome2 = %s\n", nome2);
    printf("nome3 = %s\n", nome3);
    

    return 0;
}