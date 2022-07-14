#include <stdio.h>
#include <stdlib.h>

//protótipo da função média
float media(int n, float *vnotas);
//passa um vetor para a função, utilizando-se um ponteiro como parâmetro da função

int main()
{
	float vnotas[10];
	float media_notas;
	int i;
	
	// leitura das notas
	for (i = 0; i < 10; i++) 
	{
		printf("Digite os valores das notas: ");
		scanf("%f", &vnotas[i]);
	}
	//chamada da funcao
	media_notas = media(10, vnotas);
	
	printf("\n Media das notas = %.1f", media_notas);
	
	return 0;
}

// funcao para o calculo da media
float media(int n, float *vnotas)
{
	int i; 
    float m = 0, soma = 0;
	
	//somatoria
	for(i = 0; i < n; i++)
		soma = soma + vnotas[i];
		
	// dividindo pela quantidade  de elementos n
	m = soma/n;
	
	//retorna media
	return m;
}

￼