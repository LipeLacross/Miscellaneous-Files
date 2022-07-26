using System;

namespace HelloWorld {
    class Program {
        static void Main(string[] args)
        {
            if (condition1)
            {
            // block of code to be executed if condition1 is True
            } 
            else if (condition2) 
            {
            // block of code to be executed if the condition1 is false and condition2 is True
            } 
            else
            {
            // block of code to be executed if the condition1 is false and condition2 is False
            }
            //Short Hand If...Else (Ternary Operator)
            /*There is also a short-hand if else, which is known as the ternary operator because it consists of three operands. It can be used to replace multiple lines of code with a single line. It is often used to replace simple if else statements:

            Syntax*/
            variable = (condition) ? expressionTrue :  expressionFalse;
            
            //Instead of writing:

            //Example
            int time = 20;
            if (time < 18) 
            {
            Console.WriteLine("Good day.");
            } 
            else 
            {
            Console.WriteLine("Good evening.");
            }
            
            //You can simply write:

            //Example
            int time = 20;
            string result = (time < 18) ? "Good day." : "Good evening.";
            Console.WriteLine(result);
            return 0;
        }
    }   
}