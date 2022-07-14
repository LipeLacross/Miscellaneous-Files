#include <stdio.h>
#include <stdlib.h>

/*Sintaxe:
fgetc(ponteiro_do_arquivo);
*/
int main()
{
    FILE *pont_arq;
    char c;

    pont_arq = fopen("arquivo1.txt", "r");
    //verificando se houve erro
    if (pont_arq == NULL)
    {
        printf("Erro ao tentar abrir o arquivo!");
        exit(1); //para abortar a execução
    }
    printf("Lendo e exibindo os dados do arquivo \n\n");

    //Faça
    do
    {
        //faz a leitura do caracter no arquivo apontado por pont_arq
        c = fgetc(pont_arq);

        //exibe o caracter lido na tela
        printf("%c", c);
    } while (c != EOF); //enquanto não for final de arquivo
    //EOF = END OF FILE

    fclose(pont_arq); //fechando o arquivo

    return (0);
}