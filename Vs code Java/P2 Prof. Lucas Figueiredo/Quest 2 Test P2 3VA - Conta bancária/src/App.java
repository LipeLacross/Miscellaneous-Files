/*Questão 2: Crie uma classe para representar uma Conta de um usuário de banco, com os dados incluindo nome, CPF, RG, conta corrente, agência e saldo e os métodos para imprimir o saldo, e fazer uma transferência para outra conta (caso exista saldo). Crie dois objetos desta classe, e realize uma transferência de um para outro.*/
public class App 
{
    public static void main(String[] args) throws Exception 
    {
        Conta felipeMoreira = new Conta("Felipe Moreira Rios", "19114213554", "74569826", "74856925-4", "0001" , 200);

        Conta lucasFigueiredo = new Conta("Lucas Figueiredo Da Silva", "785168946", "35629475", "95430498-1", "0001", 3);
        
        felipeMoreira.printInvoice(felipeMoreira);
        System.out.println("...");
        lucasFigueiredo.printInvoice(lucasFigueiredo);

        felipeMoreira.transfer(felipeMoreira, lucasFigueiredo, 100);
        System.out.println("...");
        lucasFigueiredo.transfer(lucasFigueiredo, felipeMoreira,2000);
    }
}