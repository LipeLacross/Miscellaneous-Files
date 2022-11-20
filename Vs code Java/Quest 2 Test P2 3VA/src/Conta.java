public class Conta {
    
String name, cpf, rg, currentAccount, agency;
double exchange, valueTransfer;
    
    public Conta(String name, 
                String cpf, 
                String rg, 
                String currentAccount, 
                String agency,
                double exchange) 
    {
        this.name = name;
        this.cpf = cpf;
        this.rg = rg;
        this.currentAccount =  currentAccount;
        this.agency = agency;
        this.exchange = exchange;
    }
    
    public void printInvoice(Conta conta)
    {
    System.out.println("============================");
    System.out.println("Nome:" + conta.name);
    System.out.println("Cpf:" + conta.cpf);
    System.out.println("Rg:" + conta.rg);
    System.out.println("Conta corrente:" + conta.currentAccount);
    System.out.println("Agência:" + conta.agency);
    System.out.println("Saldo:" + conta.exchange);
    }
    
    public void transfer(Conta origin, Conta destiny, double valueTransfer)
    {
        System.out.println("=============Transferência=============");
        System.out.println("De:" + origin.name + " " + "Cpf: " + origin.cpf + " " + "Rg: " + origin.rg);
        System.out.println("=======================================");
        System.out.println("Para: " + destiny.name + " " + "Cpf: " + destiny.cpf + " " + "Rg: " + destiny.rg);
        System.out.println("Agência: " + destiny.agency + " " + "Conta: " + destiny.currentAccount);
        System.out.println("=======================================");
        if (origin.exchange > valueTransfer)
        {
            origin.exchange = origin.exchange - valueTransfer;
            System.out.println("Transferência realizada com sucesso.");
            System.out.println("Seu saldo atual é: " + origin.exchange);
        } else
        {
            System.out.println("Não possui saldo suficiente para efetuar essa transação.");
            System.out.println("Seu saldo atual é: "  + origin.exchange);
        }
    }
}
