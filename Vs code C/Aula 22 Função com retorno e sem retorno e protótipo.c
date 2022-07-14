#include <stdio.h>
#include <stdlib.h>

/*
Esqueleto de uma função:
tipo_de_retorno nome_da_função (listagem de parâmetros)
{
    instruções;
    retorno_da_função;
}
*/

/******* Área dos protótipos ******
void imprime_cabec(void);
int multiplica(int N1, int N2);
//para poder declarar funções depois da função main
*/

void estilo()//função sem retorno a ser invocada posteriormente
{
    printf("==================================\n");
    return; //não retorna nada, logo coloca-se apenas o return
}
int multiplica(int n1, int n2) //função com retorno a ser invocada posteriormente
{
    int res;
    res = n1 * n2;
    return res;
}
int main()
{
    int V1, V2, resultado;

    estilo();
    printf("Digite o primeiro valor:");
    scanf("%d", &V1);
    printf("Digite o segundo valor:");
    scanf("%d", &V2);
    estilo();

    //chama a função e recebe o retorno
    resultado = multiplica(V1, V2);

    printf("Resultado = %d\n", resultado);
    estilo();
    
    return 0;
}