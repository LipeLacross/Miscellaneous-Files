#include <stdio.h>
#include <stdlib.h>

/*
Sintaxe:
switch (variável)
{
   case constante1:
     Instruções;
   break;

   case constante2:
     Instruções;
   break;

   default:
     Instruções;
}
A instrução break termina a execução do switch e o programa continua a executar na instrução seguinte.

O uso do break evita testar as demais alternativas de forma desnecessária quando uma opção verdadeira já foi encontrada.

O comando default exibe uma mensagem, caso nenhuma das alternativas anteriores seja verdadeira.
*/
int main()
{
  int valor = 1;

  while (valor <= 7 && valor >= 1)
  {
    printf("Digite um valor de 1 a 7: ");
    scanf("%d", &valor);
    
    switch (valor)
    {
    case 1:
      printf("Domingo\n");
      break;

    case 2:
      printf("Segunda\n");
      break;

    case 3:
      printf("Terça\n");
      break;

    case 4:
      printf("Quarta\n");
      break;

    case 5:
      printf("Quinta\n");
      break;

    case 6:
      printf("Sexta\n");
      break;

    case 7:
      printf("Sabado\n");
      break;

    default:
      printf("Valor invalido!\n");
    }
  }
  return 0;
}
