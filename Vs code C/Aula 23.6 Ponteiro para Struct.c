#include <stdio.h>
#include <stdlib.h>

typedef struct tAluno
{
    int matricula;
    float nota;
} tAluno;

int main()
{
    //a1 é uma struct do tipo tAluno
    tAluno a1;

    //*ptrAluno é um ponteiro do tipo tAluno que recebe o endereço de a1
    tAluno *ptrAluno = &a1;

    //atribuindo valores para os membros do struct a1
    a1.matricula = 555;
    a1.nota = 8.0;

    //exibindo dados usando a struct diretamente
    printf("matrícula: %d nota: %.2f\n", a1.matricula, a1.nota);

    //podemos atribuir ou acessar um valor usando o ponteiro (*ptrAluno)
    (*ptrAluno).nota = 8.5;
    (*ptrAluno).matricula = 455;

    //exibindo dados um ponteiro para struct
    printf("\nmatricula: %d nota: %.2f \n", (*ptrAluno).matricula, (*ptrAluno).nota);

    //prtAluno-> substitui a notação (*ptrAluno). de forma mais intuitiva
    //atribuindo novo valor 
    ptrAluno->nota = 9;
    ptrAluno->matricula = 355;
    
    printf("\nmatricula: %d nota: %.2f \n", ptrAluno->matricula, ptrAluno->nota);

    return 0;
}