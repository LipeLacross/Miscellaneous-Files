/*Crie um programa com as quatro funções a seguir:
Potência ------------  	(a partir de dois números inteiros n e p)
	Fatorial -------------  	(a partir de um número inteiro n)
	Permutação --------	(a partir de dois números inteiros n e r)
	Combinatória -------	(a partir de dois números inteiros n e r)
	Polinômio Binomial* -	(a partir de um número inteiro n)
	Curva de Bézier* ----	(a partir de um número inteiro n)
Por mensagem de texto o programa oferece as funções, o usuário digita um número de 1 a 6 para escolher a operação, e em seguida digita os parâmetros.
*nesses casos o programa deve mostrar a fórmula completa
*/
using System;

namespace HelloWorld {
	class Program {
		public static void Main(string[] args) {
			string escolha1 = "", escolha2, escolha3, valor1, valor2, valor3, valor4, valor5, enter;
			int convertido1, convertido2, convertido3, convertido4;

			while (escolha1 != "7") {
				
				Console.WriteLine("================================================================================================\nCalculadora de potência, permutação, combinatória, polinômio binomial e curva de bézier.\n================================================================================================\nEscolha o número do tipo cálculo:\nPotência(1)\nFatorial(2)\nPermutação(3)\nCombinatória(4)\nPolinômio Binomial(5)\nCurva de Bézier(6)\nFechar aplicativo(7)");
				escolha1 = Console.ReadLine();
				var mat = new Mat();

				//Potência
				if (Convert.ToInt64(escolha1) == 1) { //Vai converter a string escolha em int
					Console.WriteLine("Escolha um número inteiro:");
					valor1 = Console.ReadLine();
					Console.WriteLine("Escolha um número inteiro para elevar número escolhido:");
					valor2 = Console.ReadLine();
					Console.WriteLine("a^n = a * a * a * a ... n vezes.");
					convertido1 = Convert.ToInt32(valor1);
					convertido2 = Convert.ToInt32(valor2);
					Console.WriteLine($"A potência de {valor1} elevado a {valor2} é igual a {(mat.potencia(convertido1, convertido2))}.");
					//Console.WriteLine(mat.potencia(convertido1, convertido2));
				} else if (Convert.ToInt64(escolha1) == 2) { //Fatorial
					Console.WriteLine("Escolha um número inteiro:");
					valor1 = Console.ReadLine();
					Console.WriteLine("n! = n * (n – 1)*(n – 2)*(n – 3) ... * 1");
					convertido1 = Convert.ToInt32(valor1);
					Console.WriteLine($"O fatorial de {valor1} é {(mat.fatorial(convertido1))}.");
				} else if (Convert.ToInt64(escolha1) == 3) { //Permutação
					Console.WriteLine("A ordem dos elementos importa.\nTem repetição de elementos? (1)-Sim, (2)-Não:");
					escolha2 = Console.ReadLine();
					
					if (Convert.ToInt64(escolha2) == 2) {
						Console.WriteLine("Escolha um número inteiro que represente a quantidade total de elementos:");
						valor1 = Console.ReadLine();
						Console.WriteLine("n! = n * (n – 1)*(n – 2)*(n – 3) ... * 1");
						convertido1 = Convert.ToInt32(valor1);
						Console.WriteLine($"A permutação de {valor1} é {(mat.fatorial(convertido1))}.");
					} else if (Convert.ToInt64(escolha2) == 1) {
						Console.WriteLine("Escolha um número inteiro que represente a quantidade total de elementos:");
						valor1 = Console.ReadLine();
						Console.WriteLine("Quantos elementos tem repetições(máximo 3)");
						escolha3 = Console.ReadLine();
						
						if (Convert.ToInt64(escolha3) == 1) {
						Console.WriteLine("Digite a quantidade repetições de um elemento:");
						valor2 = Console.ReadLine();
						convertido1 = Convert.ToInt32(valor1);
						convertido2 = Convert.ToInt32(valor2);
						
						} else if (Convert.ToInt64(escolha3) == 2) {
						Console.WriteLine("Digite a quantidade repetições de um elemento:");
						valor2 = Console.ReadLine();
						Console.WriteLine("Digite a quantidade repetições de um outro elemento:");
						valor3 = Console.ReadLine();

						convertido1 = Convert.ToInt32(valor1);
						convertido2 = Convert.ToInt32(valor2);
						convertido3 = Convert.ToInt32(valor3);
						} else if (Convert.ToInt64(escolha3) == 3) {
						Console.WriteLine("Digite a quantidade repetições de um elemento:");
						valor2 = Console.ReadLine();
						Console.WriteLine("Digite a quantidade repetições de um outro elemento:");
						valor3 = Console.ReadLine();
						Console.WriteLine("Digite a quantidade repetições de um último outro elemento:");
						valor4 = Console.ReadLine();

						convertido1 = Convert.ToInt32(valor1);
						convertido2 = Convert.ToInt32(valor2);
						convertido3 = Convert.ToInt32(valor3);
						convertido4 = Convert.ToInt32(valor4);
						} else {
							Console.WriteLine("ESCOLHA UM DOS NÚMEROS!!!");
							break;
						}
						convertido1 = Convert.ToInt32(valor1);
						convertido2 = Convert.ToInt32(valor2);
						convertido3 = Convert.ToInt32(valor3);
						convertido4 = Convert.ToInt32(valor4);
			
						Console.WriteLine($"Se um conjunto, com n elementos, possui k repetições de um elemento, a fórmula assume a seguinte forma: P = n!/k!, logo a permutação de {valor1} elementos com {valor2} elementos(iguais) repetidos é igual a {(mat.permuta(convertido1, convertido2, convertido3))}.");
					} else {
						Console.WriteLine("ESCOLHA UM DOS NÚMEROS!!!");
						break;
					}
				} else if (Convert.ToInt64(escolha1) == 4) { //Combinatória
					Console.WriteLine("A ordem dos elementos não importa");
					Console.WriteLine("Escolha um número inteiro que represente a quantidade total de elementos:");
						valor1 = Console.ReadLine();
						Console.WriteLine("Digite a quantidade repetições de um elemento:");
						valor2 = Console.ReadLine();
						convertido1 = Convert.ToInt32(valor1);
						convertido2 = Convert.ToInt32(valor2);
						Console.WriteLine($"Se em um conjunto, com n elementos, k serão selecionados, a fórmula assume a seguinte forma: C = n!/k!*(n - k)!, logo a combinação de {valor1} elementos com {valor2} elementos selecionados é igual a {(mat.combination(convertido1, convertido2))}.");
				} else if (Convert.ToInt64(escolha1) == 5) { //Polinômio Binomial
					Console.WriteLine("Escolha um número inteiro:");
					valor1 = Console.ReadLine();
					Console.WriteLine("n! = n . (n – 1).(n – 2).(n – 3)… . 1");
					convertido1 = Convert.ToInt32(valor1);
					Console.WriteLine($"Se queremos somar dois termos em parêntese elevados a um número, logo se elevarmos esses termos por {valor1} o resultado será {(mat.polibinomial(convertido1))}.");
				} else if (Convert.ToInt64(escolha1) == 6) { //Curva de Bézier
					Console.WriteLine("Escolha um número inteiro para o índice t:");
					valor1 = Console.ReadLine();
					Console.WriteLine("n! = n . (n – 1).(n – 2).(n – 3)… . 1");
					convertido1 = Convert.ToInt32(valor1);
					Console.WriteLine("Qual será o tipo de curva?\nCurva linear(1), quadrática(2), ou cúbica(3)");
					escolha2 = Console.ReadLine();
					if (escolha2 == "1") {
						Console.WriteLine($"O indíce {valor1} {(mat.curvaBezierLinear(convertido1))}.");
					} else if (escolha2 == "2") {
						Console.WriteLine($"O indíce {valor1} {(mat.curvaBezierLinear(convertido1))}.");
					} else if (escolha2 == "3") {
						Console.WriteLine($"O indíce {valor1} {(mat.curvaBezierLinear(convertido1))}.");

					}
				} else if (Convert.ToInt64(escolha1) == 7) { //Fechar Aplicativo
					Console.WriteLine("Fechando aplicativo...");
					System.Environment.Exit(1);
				} else {
					Console.WriteLine("ESCOLHA UM DOS NÚMEROS!!!");
				}
			Console.WriteLine("Pressione enter pra continuar");
			enter = Console.ReadLine();
			}
		}

	}
	
}