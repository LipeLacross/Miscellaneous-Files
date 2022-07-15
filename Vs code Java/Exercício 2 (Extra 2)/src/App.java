import java.util.Scanner;

public class App {
    public static int multi(int n, int p) {
        int resultado = 0;
        
        for (int i = 0; i < p; i++) {
            resultado = resultado + n; 
        }
        
        return resultado;
    }        
    
    public static int potencia(int n, int p) {
        int resultado = 1;

        for (int i = 0; i < p; i++) {
            resultado = multi(resultado, n);
        }
        
        return resultado;
    }        
    
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        int numero, potencia;
        System.out.println("Digite o número base e depois o número para potenciar.");
        numero = scan.nextInt();
        potencia = scan.nextInt();
        
        int resultado = potencia(numero, potencia);
        int resultado2 = multi(numero, potencia);
        
        System.out.println(numero + " elevado a " + potencia + " tem como resultado: " + resultado);
        System.out.println(resultado2);
        scan.close();
    }
}
