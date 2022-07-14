#include <stdio.h>
#include <stdlib.h>

/*
Sintaxe para conter diversas outras variáveis normalmente de tipos diferentes:
struct <identificador>
{
 <listagem dos tipos e membros>;
};
struct <identificador> <variavel>;
*/
int main()
{
    struct ficha_aluno
    {
        char nome[40];
        int numero;
        float nota;
    };

    struct ficha_aluno aluno1;

    printf("\nCadastro de aluno\n\n");

    printf("Nome do aluno: ");
    fgets(aluno1.nome, 40, stdin);

    printf("Digite o número do aluno");
    scanf("%d", &aluno1.numero);

    printf("Digite a nota do aluno: ");
    scanf("%f", &aluno1.nota);

    printf("\nLendo os dados da struct\n");
    printf("Nome: %s", aluno1.nome);
    printf("Número: %i\n", aluno1.numero);
    printf("Nota: %.2f\n", aluno1.nota);

    return 0;
}