#include <stdio.h>

/*
Os operadores lógicos são:
&&     (E)
||       (OU)
!        (NÂO)
Para o operador &&  (E) o resultado será verdadeiro 
caso todas as comparações sejam  verdadeiras.

Usando o operador || (OU) o resultado será verdadeiro
bastando apenas uma das comparações ser verdadeira.

O operador lógico de negação ! (NÂO) é utilizado para 
inverter o resultado de uma determinada condição. 
Ou seja, se a condição for verdadeira esta torna-se falsa, 
e se a condição for falsa ela torna-se verdadeira.
*/


int main()//Ex: &&
{
    float nota_final, frequencia;
    printf("Digite a nota final do aluno: ");
    scanf("%f", &nota_final);
    printf("Informe a frequencia do aluno: ");
    scanf("%f", &frequencia);
    //se(nota_final > 6.0 && frequencia >= 75)
    if (nota_final > 6.0 && frequencia >= 75)
        printf("Aluno aprovado \n");
    else
        printf("Aluno reprovado \n");
    return (0);
}
/*
int main(void)//Ex:||
{
    float limite_min = 5.0, limite_max = 12.0, temperatura;
    printf("Informe o valor da temperatura: ");
    scanf("%f", &temperatura);
    if (temperatura > limite_max || temperatura < limite_min)
        printf("Temperatura OK \n");
    else
        printf("Alerta: Temperatura fora da faixa permitida!!! \n");
    return (0);
}

int main(void)//Ex: !
{
    float limite_min = 5.0, limite_max = 12.0, temperatura;
    printf("Informe o valor da temperatura: ");
    scanf("%f", &temperatura);
    //se(temperatura > limite_max OU temperatura < limite_min)
    //! vai procurar saber se uma das condições é falsa
    if (!(temperatura > limite_max || temperatura < limite_min))//bota fora da condição
        printf("Alerta: Temperatura fora da faixa permitida!!! \n");
    else
        printf("Temperatura OK \n");
    return (0);
}
*/