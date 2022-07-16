import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        
        String escolha1, escolha2, escolha3, escolha4, escolha5;
        String error = "ESCOLHA!!!";
        //int a = 0;

        System.out.println("Você é um soldado do reino de Drazio, sua missão é defender o castelo a qualquer custo. Seu nome é: ");
        String nome = input.nextLine();
    
        System.out.println("Acorde " + nome + "! O castelo está sendo atacado! Diz o capitão. \nVocê vai continuar dormindo(dormir) ou vai partir para a batalha?(lutar)");
        escolha1 = input.nextLine();

        switch (escolha1) {
            case "dormir":
                //a = 1;
                System.out.println("Você dormiu, mas infelizmente o barulho está tão alto lá fora que o seu sono se esvai. Você preguiçosamente se levanta e sai de sua cabana para verificar as armas restantes... Infelizmente já pegaram todas as armas.\n Desesperadamente você se lembra dos treinos de Muai Thay(mt) e karatê(kt) que você teve com sua avó, mas fica em dúvida sobre qual escolher.");
                escolha2 = input.nextLine();
                    
                switch(escolha2) {
                    case "mt":
                        System.out.println("Você");
                    case "kt":
                        System.out.println("Você");
                    break;
                }
                    
            case "lutar":
                //a = 1;
                System.out.println("Você corajosamente se levanta com sangue no olho e corre ansiosamente em busca do seu equipamento. Sua pressa é crucial e lhe faz encontrar algumas restantes...\nSobrou apenas um arco com duas flechas(arco) e uma espada(espada). ");
                escolha2 = input.nextLine();

                switch(escolha2) {
                    case "espada":
                        System.out.println("Você");
                    case "arco":
                        System.out.println("Você");
                }
                    break;
            default:
                System.out.println(error);
        }
        
        input.close();
    }
}
