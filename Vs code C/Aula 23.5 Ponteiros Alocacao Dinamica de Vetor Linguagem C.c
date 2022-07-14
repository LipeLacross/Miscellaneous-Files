#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *p; //criando um ponteiro para o vetor
    int i, quant_elementos;

    //recebendo a quantidade de elementos
    printf("Digite a quantidade de elementos do vetor: ");
    scanf("%d", &quant_elementos); //isso é alocação dinâmica

    //alocando a memória para o vetor de acordo\
    com a quantidade de elementos do vetor
    p = (int *)malloc(quant_elementos * sizeof(int));
    //int * para transformar p em vetor de inteiros
    //A função malloc aloca um espaço de memória e\
    retorna um ponteiro do tipo void para o início do espaço de memória alocado.

    //caso nao seja possível alocar memória suficiente enviar mensagem e sair\
    do programa com exit(1)
    if (p == NULL)
    {
        printf("\nErro de alocação de memória");

        exit(1);
    }
    printf("\n");

    //recebendo os dados para o vetor
    for ( i = 0; i < quant_elementos; i++)
    {
        printf("Digite o número para o índice [%d]: ", i);
        scanf("%d", &p[i]);
    }
    printf("\n");
    
    //percorre o vetor mostrando o s valores armazenados
    for ( i = 0; i < quant_elementos; i++)
    {
        printf("Valor armazenado no elemento de índice [%d] =  %d\n", i , p[i]);
    }
    printf("\n");
    
    //liberando memória que foi alocada
    free(p);

    return 0;
}
