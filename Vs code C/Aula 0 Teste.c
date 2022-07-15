#include <stdio.h>
//#include <stdlib.h>//Stdlib.h é uma biblioteca de propósito geral padrão.\
Ela possui funções envolvendo alocação de memória, controle de processos, conversões e outras.

int main(){
    int a,b;
    a = 0;
    b = 0;

    while(a <= 10){
        printf("corno %i\n", b);
        ++a;
        ++b;
    }
    return 0;
}