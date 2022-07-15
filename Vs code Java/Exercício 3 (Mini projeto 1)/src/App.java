import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        
        String escolha1, escolha2, escolha3, escolha4, escolha5;
        String error = "ESCOLHA!!!";
        int a = 0;

        System.out.println("Você é um soldado do reino de Drazio, sua missão é defender o castelo a qualquer custo. Seu nome é: ");
        String nome = input.nextLine();
        
        System.out.println("Acorde " + nome + "! O castelo está sendo atacado!" + 
        "Você vai continuar dormindo(dormir) ou vai se partir para a batalha?(lutar)");

        
        while (a == 0) {
            escolha1 = input.nextLine();

            switch (escolha1) {
                case "dormir":
                    System.out.println("Você dormiu");
                    escolha2 = input.nextLine();
                    a = 1;
                    switch(escolha2) {
                        case "":

                        ;
                    }
                case "lutar":
                    System.out.println("Você lutou");
                    escolha2 = input.nextLine();
                    a = 1;
                    switch(escolha2) {
                        case "":

                        ;
                    }
                    ;
                default:
                    System.out.println(error);
            }
        }
        
        input.close();
        }
    }
