public class App {
    public static void main(String[] args) throws Exception {
        if (condition1) {
            // block of code to be executed if condition1 is true
        } else if (condition2) {
            // block of code to be executed if the condition1 is false and condition2 is true
        } else {
            // block of code to be executed if the condition1 is false and condition2 is false
        }
        Short Hand If...Else
        /*There is also a short-hand if else, which is known as the ternary operator because it consists of three operands.

        It can be used to replace multiple lines of code with a single line, and is most often used to replace simple if else statements:

        Syntax*/
        variable = (condition) ? expressionTrue :  expressionFalse;
        //Instead of writing:

        //Example
        int time = 20;
        if (time < 18) {
                System.out.println("Good day.");
        } else {
                System.out.println("Good evening.");
        }

        //You can simply write:

        //Example
        int time = 20;
        String result = (time < 18) ? "Good day." : "Good evening.";
        System.out.println(result);
    }
}
