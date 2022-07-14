#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *pont_arq;
    int r;
    char texto_str[51];
    
    //abrindo o arquivo para gravação
    pont_arq = fopen("arquivo2.txt", "w");
    //testando se há erro de arquivo
    if (pont_arq == NULL)
    {
        printf("Error ao tentar abrir o arquivo!");
        exit(1); //para abortar o programa
    }

    //gravando strings no arquivo
    r = fputs("Programação em c", pont_arq);

    //verificando se os dados foram gravados
    if (r == EOF)
    {
        printf("Error ao tentar gravar os dados!");
        exit(1); //para abortar o programa
    }
    else
    {
        printf("Dados gravados com sucesso!");
    }

    //fechando o arquivo
    fclose(pont_arq);

    printf("\n ---- Leitura dos dados gravados no arquivo ----\n");

    //abrindo o arquivo para Leitura
    pont_arq = fopen("arquivo2.txt", "r");

    //enquanto não for fim de arquivo o looping será executado
    //e será lido o conteúdo do arquivo e impresso na tela com printf
    while(fgets(texto_str, 50, pont_arq) != NULL)
    {
        printf("%s\n", texto_str);
    }
    
    return (0);
}