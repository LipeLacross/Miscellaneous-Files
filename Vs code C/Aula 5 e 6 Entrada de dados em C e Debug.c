#include <stdio.h>
#include <stdlib.h>

void limpar_entrada() //pode ser invocado novamente no algaritmo
{
  char c;
  while ((c = getchar()) != '\n' && c != EOF) {}
}
int main()
{
  int idade;
  char sexo;
  char nome[20];// ou char nome[ ];
  float altura;
  double salario;

  printf("Idade: ");
  scanf("%d", &idade);
  printf("sexo: ");
  scanf(" %c", &sexo); //no scanf de %c precisa de espaço
  printf("nome: ");
  limpar_entrada();//para impedir o enter anterior e funcionar o fgets 
  fgets(nome, 50, stdin);//para botar o nome completo
  strtok(nome, "\n");//para não saltar linha
  //scanf("%s", &nome);//& não é necessário em char de string\
  não é possível botar o nome completo com esse método

  printf("altura: ");
  scanf("%f", &altura);
  printf("salario: ");
  scanf("%lf", &salario);

  printf("%s é do sexo %c, tem %i anos, tem %.2f de altura e ganha %.2lf", nome, sexo, idade, altura, salario);
}//O Placeholder do printf deve ser igual ao do scanf

/*
#include <string.h> //para funfar fgets e strtok
//f5 para fazer debugger
//é preciso botar o ponto breakpoint do lado\
para estabelecer o limite

void limpar_entrada() //pode ser invocado novamente no algaritmo
{
  char c;
  while ((c = getchar()) != '\n' && c != EOF) {}
}
//com
void texto(char *buffer, int length)
{
  fgets(buffer, length, stdin);
  strtok(buffer, "\n");
}
 limpar_entrada(); //para funcionar o fgets ou void texto
  //fgets(nome, 50, stdin);//para botar o nome completo
  //strtok(nome, "\n");//para não saltar linha
  texto(nome, 50);// para substituir os 2 comandos acima
  */