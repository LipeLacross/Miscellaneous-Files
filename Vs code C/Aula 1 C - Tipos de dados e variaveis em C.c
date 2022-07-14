#include <stdio.h>
#include <stdlib.h>
//#include <string.h>//para funcionar strcpy

int main()
{
    /*
    int, para números inteiros utiliza 4 bytes;
    char, para caracteres individuais do padrão ASCII, utiliza 1 byte;
    float, para reais entre utiliza 6 bytes, precisão de 8 dígitos;
    double, para reais entre utiliza 8 bytes, precisão de 15 dígitos;
    */

    int idade;
    float salario, altura;
    double grandenumero;
    char genero;
    char nome[50] = "maria silva"; //pode receber até 50 caracteres
    //a variável pode ser definida após a determinar o tipo de variáve\
    Ex:(Variável) (nomedavariavel) = (valor);

    idade = 20;
    salario = 5800.5, altura = 1.63;
    grandenumero = 4544545454554545;
    genero = 'f'; //aspas simples por ser do tipo char

    //nome = "Maria silva";//desse jeito string não aceita
    //strcpy(nome, "maria silva");//para string dar certo

    printf("IDADE = %i\n", idade);
    printf("SALARIO = %.2f\n", salario);
    printf("ALTURA = %.2f\n", altura);
    printf("GRANDENUMERO = %lf\n", grandenumero);
    printf("GENERO = %c\n", genero);
    printf("NOME = %s\n", nome); //utiliza-se string

    return 0;
}
