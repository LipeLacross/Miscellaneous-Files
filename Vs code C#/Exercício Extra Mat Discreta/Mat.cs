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
    public int permuta(int a, int b, int c, int d) {
        //var mat = new Mat();
        int n, k, l, m; 
        n = (fatorial(a));
        Console.WriteLine("============");
        
        if (b != null) {
            k = (fatorial(b));
            resposta = n / k;
        }
        if (c != null) {
            l = (fatorial(c));
            resposta = n / k*l;
        }
        if (d != null) {
            m = (fatorial(d));
            resposta = n / k*l*m;
        }

        return resposta;

        /*int n, k;
        int fator1 = a;
        n = 1;
        while (fator1 != 1) {
            n = n * fator1;
            fator1 -= 1;
            Console.WriteLine(n + " * " + fator1);
        }
        int fator2 = b;
        k = 1;
        while (fator2 != 1) {
            k = k * fator2;
            fator2 -= 1;
            Console.WriteLine(k + " * " + fator2);
        }*/
    }
    public int combination(int a , int b) {
        
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