#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x, *ptrx, **pptrx;

    //inicializando a variavel com zero
    x = 0;
    printf("\nvalor de x = %d\n", x);
    printf("Endereco de x: %x\n\n", &x);

    //Atribuindo os enderecos para os ponteiros
    ptrx = &x;     // ptrx aponta para x
    pptrx = &ptrx; // pptrx aponta para ptrx
\
    printf("\nvalor de x = %d", x);
    printf("\nEndereço de memória apontado por *ptrx: %x\n", ptrx);
    printf("Valor da variável X que esta sendo apontada por ptrx: %d\n", *ptrx);
    printf("Endereço de memória da variável *ptrx %x\n", &ptrx);
    //%x para imprimir endereço de memória
    printf("\n\nvalor de x = %d", x);
    printf("\nEndereço de memória apontado por **pptrx: %x", pptrx);//
    printf("\nValor da variável para a qual pptrx faz referência: %d", **pptrx);
    printf("\nEndereço de memória da variável **pptrx %x\n\n", &pptrx);

    return 0;
}