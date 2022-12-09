'''
==Operadores Aritméticos Python==
Operadores aritméticos são usados com valores numéricos para realizar operações matemáticas comuns:

Operator	Name	    Example
+	    Addition	    x + y	
-	    Subtraction	    x - y	
*	    Multiplication	x * y	
/	    Division	    x / y	
%	    Modulus	        x % y	
**	    Exponentiation	x ** y	
//	    Floor division	x // y	

==Operadores de atribuição python==
Os operadores de atribuição são usados para atribuir valores às variáveis:

Operator	Example	    Same 
=	        x = 5	    x = 5	
+=	        x += 3	    x = x + 3	
-=	        x -= 3	    x = x - 3	
*=	        x *= 3	    x = x * 3	
/=	        x /= 3	    x = x / 3	
%=	        x %= 3	    x = x % 3	
//=	        x //= 3	    x = x // 3	
**=	        x **= 3	    x = x ** 3	
&=	        x &= 3	    x = x & 3	
|=	        x |= 3	    x = x | 3	
^=      	x ^= 3	    x = x ^ 3	
>>=	        x >>= 3	    x = x >> 3	
<<=	        x <<= 3 	x = x << 3	

==Operadores de comparação python==
Os operadores de comparação são usados para comparar dois valores:

Operator	Name	                Example	
==	        Equal	                x == y	
!=     	Not equal	                x != y	
>	    Greater than	            x > y	
<	    Less than	                x < y	
>=      Greater than or equal to    x >= y	
<=	    Less than or equal to	    x <= y	

==Operadores lógicos Python==
Operadores lógicos são usados para combinar declarações condicionais:

Operator    Description	                                                    Example
and 	    Returns True if both statements are true	                    x < 5 and  x < 10	
or	        Returns True if one of the statements is true	                x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true	        not(x < 5 and x < 10)	

==Operadores de Identidade Python==
Os operadores de identidade são usados para comparar os objetos, não se forem iguais, mas se eles forem realmente o mesmo objeto, com o mesmo local de memória:

Operator	Description	                                                    Example	
is 	        Returns True if both variables are the same object	            x is y	
is          not	Returns True if both variables are not the same object	    x is not y	

==Operadores de Membros Python==
Os operadores de associação são usados para testar se uma sequência é apresentada em um objeto:

Operator	Description	                                                                        Example	
in 	        Returns True if a sequence with the specified value is present in the object	    x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y
'''

print(5 % 3)
print(-2 * -5)