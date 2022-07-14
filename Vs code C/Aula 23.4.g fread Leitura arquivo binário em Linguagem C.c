#include <stdio.h>
#include <stdlib.h>

/* Testando a função fread - Lê um arquivo binário contendo
2 vetores de 15 elementos cada um: O primeiro vetor é de 
caracteres e o segundo é de variáveis inteiras*/
/*Sintaxe: 
fread(&<variavel>, <núm_bytes>, <núm_registros>, <arquivo>);
*/
int main()
{
    char ch[15];
    int valor[15];
    int i = 0;

    //ponteiro para o arquivo
    FILE *ptrArq;

    //abertura do arquivo
    ptrArq = fopen("Binário.bin", "rb");

    //testando a criação do programa
    if (ptrArq != NULL)
    {
        printf("\n\nArquivo Binário.bin foi aberto com sucesso\n\n");
    }
    else
    {
        printf("\n\nERRO: O arquivo Binário não foi aberto e criado\n");

        exit(1);
    }
    //leitura do arquivo Binário
    //retorna o conteúdo contido em uma ocorrência do tamanho da variável ch.
    fread(ch, sizeof(ch), 1, ptrArq);
    //retorna o conteúdo contido em uma ocorrência do tamanho da variável valor.
    fread(valor, sizeof(valor), 1, ptrArq);

    printf("Vetor de caracteres: \n");

    for (i = 0; i < 15; i++)
    {
        printf("%c", ch[i]);
    }
    printf("\nVetor de inteiros: ");

    for (i = 0; i < 15; i++)
    {
        printf("\n%d", valor[i]);
    }
    //fechando o arquivo
    fclose(ptrArq);

    return 0;
}