import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        
        String escolha1, escolha2, escolha3, escolha4, situation1, situation2, situation3, situation4, situation5, situation6;
        String error = "ESCOLHA INVÁLIDA!!! VOCÊ PERDEU.";
        
        situation1 = "Você segue adiante em direção ao castelo com o propósito de defender o rei... No meio do caminho há um brutamontes com um machado.";
        situation2 = "Derrotar seu inimigo o faz pensar na condição que se encontra a realiza, você pensa se realmente vale a pena(ir) arriscar a sua vida(fugir).";
        situation3 = "Você sabe que buscar honra não o leva a nada, você foge.\nLive coward ending.";
        situation4 = "Você pensa nos prêmios e na glória que poderia receber, e diante disso vai correndo até o castelo...\nDurante sua corrida um arqueiro inimigo atira em você.";
        situation5 = "Ao entrar no castelo, você vê alguns membros do castelo mortos. Através de sua análise rápida você percebe que o rei(rei) e a princesa(princesa) podem estar vivos, porém você deve escolher quem vai procurar.";
        situation6 = "Você vai até o trono e vê o seu rei apuros, ele está cercado de inimigos. Você tenta salva-lo, entretanto é derrotado pela quantidade absurda de soldados.\nSoldier ending.";

        System.out.println("Você é um soldado do reino de Drazio, sua missão é defender o castelo.");

        System.out.println("Acorde! O castelo está sendo atacado! Diz o capitão. \nVocê vai continuar dormindo(dormir) ou vai partir para a batalha?(lutar)");
        escolha1 = input.nextLine();
        
        
        if (escolha1.toLowerCase().equals("dormir")) {
            System.out.println("Você dormiu, mas infelizmente o barulho está tão alto lá fora que o seu sono se esvai. Você preguiçosamente se levanta e sai de sua cabana para verificar as armas restantes...\nInfelizmente já pegaram todas as armas.\nDesesperadamente você se lembra dos treinos de Muai Thay(mt) e karatê(kt) que você teve com sua avó, mas fica em dúvida sobre qual escolher.");
            escolha2 = input.nextLine();
            System.out.println(situation1);

            if (escolha2.toLowerCase().equals("mt")) {
                System.out.println("Pela graça dos deuses ele está de costas pra você e sem capacete. Seu corpo é uma arma integrada, você aproveita-se da situação para chutar a cabeça do seu inimigo. Seu chute é tão forte quanto uma bigorna, e o faz desmaiar.\nInfelizmente você machucou seu pé e não pode correr.");
                System.out.println(situation2);
                escolha3 = input.nextLine();

                if (escolha3.toLowerCase().equals("fugir")) {
                    System.out.println(situation3);
                } else if (escolha3.toLowerCase().equals("ir")) {
                    System.out.println("Você pensa nos prêmios e na glória que poderia receber, e diante disso vai andando até o castelo...\nDurante sua corrida um arqueiro inimigo atira em você, já que você não tinha nenhuma armadura o resultado foi fatal...\nWarrior ending.");
                } else {
                    System.out.println(error);
                }
            } else if (escolha2.toLowerCase().equals("kt")) {
                System.out.println("Pela graça dos deuses ele está de costas pra você e sem capacete. Seu corpo é uma arma integrada, você aproveita-se da situação para pular no pescoço do seu inimigo. Com o seus braços você o enforca até ");
                System.out.println(situation2);
                escolha3 = input.nextLine();

                if (escolha3.toLowerCase().equals("fugir")) {
                    System.out.println(situation3);
                } else if (escolha3.toLowerCase().equals("ir")) {
                    System.out.println(situation4);
                    System.out.println("Graças a sua alta agilidade você não sofre nenhum dano durante o trajeto. ");
                    System.out.println(situation5);
                    
                    escolha4 = input.nextLine();

                    if (escolha4.toLowerCase().equals("rei")) {
                        System.out.println(situation6);
                    } else if (escolha4.toLowerCase().equals("princesa")) {
                        System.out.println("Você vai até o quarto da princesa e não se depara com ninguém, ao entrar no quarto você começa a procura-la...\nEla estava escondida embaixo da cama, logo você explica a situação para ela e decide fugir com ela. \n Ela diz que há uma passagem secreta em determinado lugar do castelo, enquanto olha discretamente para sua vestimenta.\nVocê a leva até o local, ela abre passagem, assim permitindo a fuga.\nMas antes ela se aproxima de você para beija-lo, e sorrateiramente esfaqueia seu pescoço.\nLogo depois ela foge sozinha. \nGado ending");
                    } else {
                        System.out.println(error);
                    }
                } else {
                    System.out.println(error);
                }
            } else {
                System.out.println(error);
            }

        } else if (escolha1.toLowerCase().equals("lutar")) { 
            System.out.println("Você corajosamente se levanta com sangue no olho e corre ansiosamente em busca do seu equipamento. Sua pressa é crucial e lhe faz encontrar algumas restantes...\nSobrou apenas um arco com duas flechas(arco), uma espada(espada) e algumas peças de armadura. ");
            escolha2 = input.nextLine();
            System.out.println(situation1);

            if (escolha2.toLowerCase().equals("arco")) {
                System.out.println("Seu inimigo olha para você e corre loucamente para ataca-lo. Você só tem duas chances de acertar a sua flecha.\nVocê mira na cabeça do seu inimigo e atira, no entanto seu inimigo se defende com o machado.\nVocê engole seco e prepara sua última flecha, sabe que se errar irá morrer...\nVocê atira e...\nAcerta!\nNa parede... logo recebe uma machadada e morre.\nBad ending.");

            } else if (escolha2.toLowerCase().equals("espada")) {
                System.out.println("Seu inimigo olha para você e corre loucamente para ataca-lo. Sua mente é perspicaz, você corre na direção do seu oponente, ele o ataca pela direita, mas você se joga no chão e desliza em baixo.\nRapidamente você vê uma brecha na virilha do seu oponente, ela se encontra desprotegida, você dá uma cotovelada no saco do brutamontes e o faz ficar atordoado e de joelhos.\nVocê aproveita-se da situação para cortar a cabeça do obeso.");
                System.out.println(situation2);
                escolha3 = input.nextLine();

                if (escolha3.toLowerCase().equals("fugir")) {
                    System.out.println(situation3);
                } else if (escolha3.toLowerCase().equals("ir")) {
                    System.out.println(situation4);
                    System.out.println("Graças a sua armadura você não sofre nenhum dano durante o trajeto.");
                    System.out.println(situation5);
                    escolha4 = input.nextLine();

                    if (escolha4.toLowerCase().equals("rei")) {
                        System.out.println(situation6);
                    } else if (escolha4.toLowerCase().equals("princesa")) {
                        System.out.println("Você vai até o quarto da princesa e não se depara com ninguém, ao entrar no quarto você começa a procura-la...\nEla estava escondida embaixo da cama, logo você explica a situação para ela e decide fugir com ela. \n Ela diz que há uma passagem secreta em determinado lugar do castelo, enquanto olha discretamente para sua vestimenta.\nVocê a leva até o local, ela abre passagem, assim permitindo a fuga.\nMas antes ela se aproxima de você para beija-lo, logo depois vocês fogem juntos.\nGood ending");
                    } else {
                        System.out.println(error);
                    }

                } else {
                    System.out.println(error);
                }
            
            } else {
                System.out.println(error);
            }

        } else {
            System.out.println(error);
        }

        input.close();
    }
}

/* BASE
        if (escolha.toLowerCase().equals("")) {
            System.out.println("");
        } else if (escolha.toLowerCase().equals("")) {
            System.out.println("");
        } else {
            System.out.println(error);
        }
        */