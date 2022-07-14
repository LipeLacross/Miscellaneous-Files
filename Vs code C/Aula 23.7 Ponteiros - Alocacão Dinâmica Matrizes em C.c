#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i, j, n_linhas, n_colunas;
    //matrizes dinâmicas de duas dimensões portanto vamos necessitar\
    de um ponteiro para a linha e outro ponteiro apontando para coluna

    int **matriz1, **matriz2, **matriz_soma;
    FILE *ptrArq;

    //abrindo arquivo
    ptrArq = fopen("ArqMatrizes.txt", "r");

    //verificando e a abertura foi bem sucedida
    if (ptrArq == NULL)
    {
        printf("Erro ao abrir o arquivo!\n");
        printf("Saindo do programa...\n");
        exit(1); //abortando o programa
    }
    //leitura das dimensões da matriza apartir dos valores do arquivo
    fscanf(ptrArq, "%d %d", &n_linhas, &n_colunas);

    //alocar memória necessária para as matrizes
    //----------------Alocando a matriz1-----------------
    matriz1 = (int **)calloc(n_linhas, sizeof(int *)); //alocar quantidade de linhas

    for (i = 0; i < n_linhas; i++)
    {
        //aloca quantidade de colunas de cada linha
        matriz1[i] = (int *)calloc(n_colunas, sizeof(int));
    }
    //----------------Alocando a matriz2-----------------
    matriz2 = (int **)calloc(n_linhas, sizeof(int *)); //alocar quantidade de linhas

    for (i = 0; i < n_linhas; i++)
    {
        //aloca quantidade de colunas de cada linha
        matriz2[i] = (int *)calloc(n_colunas, sizeof(int));
    }
    //ler os valores para as matrizes a apartir do arquivo texto
    for (i = 0; i < n_linhas; i++)
    {
        for (j = 0; j < n_colunas; j++)
        {
            fscanf(ptrArq, "%d", &matriz1[i][j]);
        }
    }

    for (i = 0; i < n_linhas; i++)
    {
        for (j = 0; j < n_colunas; j++)
        {
            fscanf(ptrArq, "%d", &matriz2[i][j]);
        }
    }
    fclose(ptrArq); //fechar arquivo

    //mostrar as matrizes lidas
    for (i = 0; i < n_linhas; i++)
    {
        for (j = 0; j < n_colunas; j++)
        {
            printf("%2d ", matriz1[i][j]);
        }
        printf("   "); //espaçamento entre as matrizes

        for (j = 0; j < n_colunas; j++)
        {
            printf("%2d ", matriz2[i][j]);
        }
        printf("\n");
    }
    //alocar memória para matriz soma
    for (i = 0; i < n_linhas; i++)
    {
        matriz_soma[i] = (int *)calloc(n_colunas, sizeof(int));
    }
    //calcular matriz soma
    for (i = 0; i < n_linhas; i++)
    {
        for (j = 0; j < n_colunas; j++)
        {
            matriz_soma[i][j] = matriz1[i][j] + matriz2[i][j];
        }
    }
    //mostrar matriz soma
    printf("\nMatriz soma:\n");

    for (i = 0; i < n_linhas; i++)
    {
        for (j = 0; j < n_colunas; j++)
        {
            printf("%3d ", matriz_soma[i][j]);
        }
    }
    printf("\n");
    return 0;
}
