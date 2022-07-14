#include <stdio.h>
#include <stdlib.h>

int main()
{
    /*
        Tipo / Placeholder de formatação
        int / %d ou %i                     
        long int / %li
        long long int / %lli
        float / %f
        double / %lf
        char / %c
        char[] / %s
        */
    //para imprimir no printf

    // /n para saltar linha e /t para tabulação

    int idade = 20;
    char sexo = 'F';
    char nome[50] = "Micael corno";
    float altura = 1.95;
    double salario = 2098;

    printf("Idade: %i\n", idade);
    printf("sexo: %c\n", sexo);
    printf("nome: %s\n", nome);
    printf("altura: %.2f\n", altura);
    printf("salario: %.2lf\n", salario);
    printf("%s é do sexo %c, tem %i anos, tem %.2f de altura e ganha %.2lf", nome, sexo, idade, altura, salario);
    //para controlar as casas decimais: %.(quantidade)(Placeholder)
    return 0;
}
