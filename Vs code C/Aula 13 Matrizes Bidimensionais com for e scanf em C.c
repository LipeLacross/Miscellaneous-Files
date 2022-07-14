#include <stdio.h>
#include <stdlib.h>

/*
Exemplo de declaração de matriz com 2 dimensões usando linguagem C
<Variável> <Nome_da_variável>[5][2];
Onde:
O valor 5 representa a quantidade de linhas.
O valor 2 representa a quantidade de colunas.
*/
int main()
{
    //int z[2][3] = {10, 20, 30, 40, 50, 60};
    //ou
    int z[2][3] = {{10, 20, 30} , {40, 50, 60}};
    //            primeira linha , segunda linha 
    printf("Valor da linha 0, coluna 0 = %d\n", z[0][0]);
    printf("Valor da linha 0, coluna 1 = %d\n", z[0][1]);
    printf("Valor da linha 0, coluna 2 = %d\n", z[0][2]);
    
    printf("\nValor da linha 1, coluna 0 = %d\n", z[1][0]);
    printf("Valor da linha 1, coluna 1 = %d\n", z[1][1]);
    printf("Valor da linha 1, coluna 2 = %d\n", z[1][2]);
    system("clear");

    int m, n, i, j;//processo automatizado com scanf

    printf("Quantas linhas vai ter na matriz? ");
    scanf("%d", &m);

    printf("Quantas colunas vai ter na matriz? ");
    scanf("%d", &n);

    int mat[m][n];

    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("Elemento [%d,%d]: ", i, j);
            scanf("%d", &mat[i][j]);
        }
    }
    printf("\nMatriz digitadas: \n");

    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("%d", mat[i][j]);
        }
        printf("\n");
    }

    return 0;
}
