/* Atividade
Crie um chatbot de cadastro de 
alguma plataforma/sistema/app
imaginário que você quiser.

Chatbot deve se apresentar
(usando ‘System.out.println’) e fazer 
perguntas para o usuário preencher.

Na sequência o chatbot deve usar as 
respostas recebidas para interagir
com o usuário e seguir com o 
preenchimento.
*/

/* Variáveis
int myNum = 5;               // Integer (whole number) 
float myFloatNum = 5.99f;    // Floating point number
char myLetter = 'D';         // Character
boolean myBool = true;       // Boolean
String myText = "Hello";     // String
*/
/* Para printar
nextBoolean()	Reads a boolean value from the user
nextByte()	Reads a byte value from the user
nextDouble()	Reads a double value from the user
nextFloat()	Reads a float value from the user
nextInt()	Reads a int value from the user
nextLine()	Reads a String value from the user
nextLong()	Reads a long value from the user
nextShort()	Reads a short value from the user
*/
/*Linguagens de programação definem operadores para manipularem os dados
Aritméticos: 	+ 	- 	* 	/ 	% 	++ 	--
Comparação: 	== 	!=	>	< 	>=	<=
Lógicos:		   &&	||	!	
Lógicos [Python]: and	or	not
Atribuição:	=	+=	-=	*=	/=	%=
Bitwise:		&	|	^	~	<<	>>
*/
/* Para mudar tipo de uma variável
Integer.ValueOf(str); //Para virar inteiro
String.valueOf(int); //Para virar string
 */
import java.util.Scanner;
public class App {
    public static void main(String[] args) {        
        Scanner escaneador = new Scanner(System.in);

        System.out.print("========================================================\n");
        System.out.println("Olá, meu nome é Dona Maria, vou prosseguir com o seu atendimento. Por favor me diga seu nome!"); //print com ln vai escrever na tela e saltar uma linha
        String nome = escaneador.nextLine();
        
        System.out.println("Olá " + nome + ", você tem um nome lindo, agora me diga qual é a sua idade?");
        int idade = escaneador.nextInt();
        escaneador.nextLine();

        if (idade >= 18) {
            System.out.println(idade + " anos, você é maior de idade, para sua felicidade o conteúdo é permitido.");
        } else {    
            System.out.println(idade + " anos, você é menor de idade, infelizmente o conteúdo está bloqueado!");
            System.exit(0);
        }
        
        System.out.println("Estamos quase acabando, agora me fale seu CPF.");
        int cpf = escaneador.nextInt();
        escaneador.nextLine();

        System.out.println("Então o seu cpf é " + cpf + "\nAgora pra finalizar, digite sua senha. Prometo que não vou contar a ninguém.");
        String senha = escaneador.nextLine();
        
        System.out.println("Prontinho, está terminado, anote sua senha:" + senha);
        System.out.print("========================================================");
        
        escaneador.close();
    }
}
    