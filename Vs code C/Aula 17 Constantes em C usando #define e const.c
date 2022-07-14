#include <stdio.h>
#include <stdlib.h>
#include <string.h>//para %s funfar
/*
Sintaxe:
#define <nome_da_constante> <valor>
ou
const <variável> <nome_da_constante> <valor>
Exemplos de declaração de constantes:
#define MAX 100
#define ERRO "Erro!!!"
ou
const int MAX = 100;
const char ERRO[30] = "error!!!";
*/

//declaração da constante
#define ICMS 0.18; //não pode ser modificado durante a execução do programa

int main(void)
{
    float preco_produto, valor_icms;
    const float frete = 10.50;
    const char final[30] = "Obrigado pela compra";

    printf("Informe o valor do produto: ");
    scanf("%f", &preco_produto);

    valor_icms = preco_produto * ICMS;

    printf("Valor de imposto a ser pago: R$ %.2f com frete de %.2f", valor_icms, frete);
    printf("\n%s", final);
    return 0;
}