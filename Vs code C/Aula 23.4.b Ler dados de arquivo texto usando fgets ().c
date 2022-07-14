#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *pont_arq;
    char texto[20];

    //abrindo o arquivo em modo leitura
    pont_arq = fopen("arquivo_palavra.txt", "r");
    
    //enquanto nao for fim de arquivo o looping será executado
    //e será impresso o texto
    while (fgets (texto, 20, pont_arq) != NULL)
    {
        printf("%s", texto);
    }

    //fechando o arquivo
    fclose(pont_arq);

    return 0;
}