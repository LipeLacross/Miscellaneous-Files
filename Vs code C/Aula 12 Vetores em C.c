#include <stdio.h>
#include <stdlib.h>

/*
Sintaxe:
Tipo NomeDoVetor[quantidade_de_itens];
Para zerar os vetores:
Tipo NomeDoVetor[ ];
*/
int main()
{                   //0  1  2    3    4    
    float notas[5] = {7, 8, 9.5, 9.9, 5.2};
    // declarando e inicializando o vetor notas

    printf("Exibindo os Valores do Vetor: \n");
    printf("notas[0] = %.1f\n", notas[0]);
    printf("notas[1] = %.1f\n", notas[1]);
    printf("notas[2] = %.1f\n", notas[2]);
    printf("notas[3] = %.1f\n", notas[3]);
    printf("notas[4] = %.1f\n", notas[4]);

    /*//para automatizar o processo com scanf
    int n, i;
    
    printf("Quantos números você vai digitar? ");
    scanf("%d", &n); //a quantidade de vetores é determinada por n

    float vet[n]; //números podem ser armazenados em vetores

    for (int i = 0; i < n; i++)
    {
        printf("Digite um numero: ");
        scanf("%f", &vet[i]);//os números digitados são retidos pelo vetor i
    }
    printf("\nNUMEROS DIGITADOS:\n");

    for (i = 0; i < n; i++)
    {
        printf("%.1f\n", vet[i]);
    }
    */
    return 0;
}
