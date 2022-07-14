#include <stdio.h>
#include <stdlib.h>
#include <string.h>//para o strtok funfar

int main()
{
    
    char nome[20]; //string é uma variável que armazena uma cadeia de caracteres
    //ou char nome [];
    printf("Digite seu nome: ");
    //scanf("%s", nome);//
    //não é possível adicionar o valor fora da variável: nome = "<Caracateres>";
    //apenas com o uso do strcpy: strcpy(nome, "Fulano");
    
    fgets(nome, 20, stdin);
    strtok(nome, "\n"); //para não saltar linha\
    e não contar o enter como elementos

    printf("O nome armazenado foi: %s\n", nome);
    for (int i = 0; nome[i] != '\0'; i++)
    {
        printf("Elemento %d: %c\n", i, nome[i]);
    }

    printf("Quantidade de caracteres: %d", strlen(nome));
    //Sintaxe para saber a quantidade de caracteres:
    //strlen(<nome_da_variável>); 
    return 0;
}
