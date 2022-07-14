#include <stdio.h>
#include <stdlib.h>

/* Testando a função fwrite - Grava um arquivo binário contendo 
2 vetores de 15 elementos cada um: O primeiro vetor armazena
caracteres e o segundo armazena dados inteiros 
*/
/*Sintaxe: 
fwrite(&<variável>, <número_de_bytes>, <número_registros>, <arquivo>);
*/
int main()
{
    char ch[15] = "Teste geral";
    int valor[15] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

    //ponteiro para o arquivo
    FILE *ptrArq;

    //abertura do arquivo
    ptrArq = fopen("Binário.bin", "wb");

    if (ptrArq != NULL)
    {
        printf("Arquivo criado com sucesso");
    }
    else
    {
        printf("Arquivo não foi aberto");
        exit(1);// para parar o programa
    }

    //gravando os dados no arquivo usando a função fwrite
    fwrite(ch, sizeof(char), 15, ptrArq); 
    fwrite(valor, sizeof(int), 15, ptrArq);

    //fechando o Arquivo
    fclose(ptrArq);

    return 0;
}