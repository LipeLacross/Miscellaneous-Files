class Mat {
    int a, b, c, d, e, f, resposta;
    
    public int potencia(int a , int b) {
        resposta = 1;
        for (int i = 1; i <= b; i++) { 
        resposta *=  a;
        }
        return resposta;
    }
    public int fatorial(int a) {
        int fator = a;
        resposta = 1;
        while (fator != 1) {
            resposta = resposta * fator;
            fator -= 1;
            Console.WriteLine(resposta + " * " + fator);
        }
        return resposta;
    }
    public int permuta1(int a, int b) {
        Console.WriteLine("n!");
        int n = fatorial(a);
        Console.WriteLine("k!");
        int k = fatorial(b);

        resposta = n/k;
        return resposta;
    }
    public int permuta2(int a, int b, int c) {
        Console.WriteLine("n!");
        int n = fatorial(a);
        Console.WriteLine("k!");
        int k = fatorial(b);
        Console.WriteLine("j!");
        int j = fatorial(c);

        resposta = n/k * j;
        return resposta;
    }
    public int permuta3(int a, int b, int c, int d) {
        Console.WriteLine("n!");
        int n = fatorial(a);
        Console.WriteLine("k!");
        int k = fatorial(b);
        Console.WriteLine("j!");
        int j = fatorial(c);
        Console.WriteLine("m!");
        int m = fatorial(d);
        
        resposta = n/k * j * m;
        return resposta;
    }
    public int combination(int a , int b) {
        Console.WriteLine("n!");
        int n = fatorial(a);
        Console.WriteLine("p!");
        int p = fatorial(b);
        Console.WriteLine("(n - p)!");
        int NP = fatorial(a - b);
        
        resposta = n/p * NP;
        return resposta;
    }
    public int polibinomial(int a) {
        
        return resposta;
    }
    public int curvaBezierLinear(int a) {
        
        return resposta;
    }
    public int curvaBezierQuadrada(int a) {
        
        return resposta;
    }
    public int curvaBezierCu(int a) {
        
        return resposta;
    }
}