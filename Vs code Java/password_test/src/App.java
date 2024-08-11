import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class App {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Digite sua senha:");
        String password = input.nextLine();
        
        if (isStrongPassword(password)) {
            System.out.println("Senha forte.");
        } else {
            System.out.println("Senha fraca.");
        }
    }
    
    public static boolean isStrongPassword(String password) {
        // Verifica se a senha tem pelo menos 8 caracteres
        if (password.length() < 8) {
            return false;
        }
        
        // Verifica se a senha contém pelo menos uma letra maiúscula, uma letra minúscula e um número
        Pattern pattern = Pattern.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).+$");
        Matcher matcher = pattern.matcher(password);
        if (!matcher.matches()) {
            return false;
        }
        
        // Verifica se a senha não contém espaços em branco
        if (password.contains(" ")) {
            return false;
        }
        
        return true;
    }
}
