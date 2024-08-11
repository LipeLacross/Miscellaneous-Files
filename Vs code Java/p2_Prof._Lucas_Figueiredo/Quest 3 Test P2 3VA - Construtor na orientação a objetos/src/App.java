/*Questão 3:  explique o que é um "construtor" no contexto de orientação a objetos. Crie uma classe que representa um Perfil do Instagram. A classe deve conter os atributos representando o nome e @ig. Crie dois construtores para esta classe, um construtor sem parâmetros e outro que recebe todos os parâmetros necessários. Usando cada um dos construtores, crie dois objetos da classe.*/
public class App {
    public static void main(String[] args) throws Exception {
        // Cria um objeto usando o construtor sem parâmetros
        Profile profile1 = new Profile();
        
        // Cria um objeto usando o construtor que recebe os parâmetros
        Profile profile2 = new Profile("fulano", "@fulano");
    }
}
