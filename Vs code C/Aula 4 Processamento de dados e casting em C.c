#include <stdio.h>
#include <stdlib.h>

int main(){
    float b1, b2, h, area;
    b1 = 6.0;
    b2 = 8.0;
    h = 5.0;
    area = (b1 + b2) / 2.0 * h; //pode-se realizar operações
    printf("%.2f\n", area);

    float a;
    int b;
    a = 5.45454545;
    b = a;
    printf("%d\n", b); //conversão para inteiro

    int x;
    float z;
    x = 5;
    z = x;
    printf("%f\n", z); //conversão para float
}