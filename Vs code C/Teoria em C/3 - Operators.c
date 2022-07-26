Arithmetic Operators
Arithmetic operators are used to perform common mathematical operations.

Operator	Name	            Description	                            Example	
+	        Addition	        Adds together two values	            x + y	
-	        Subtraction	        Subtracts one value from another	    x - y	
*	        Multiplication	    Multiplies two values	                x * y	
/	        Division	        Divides one value by another	        x / y	
%	        Modulus	            Returns the division remainder	        x % y	
++	        Increment	        Increases the value of a variable by 1	++x	
--	        Decrement	        Decreases the value of a variable by 1	--x	

Assignment Operators
Assignment operators are used to assign values to variables.

Operator	Example	    Same As	
=	        x = 5	    x = 5	
+=	        x += 3	    x = x + 3	
-=	        x -= 3	    x = x - 3	
*=	        x *= 3	    x = x * 3	
/=	        x /= 3	    x = x / 3	
%=	        x %= 3	    x = x % 3	
&=	        x &= 3	    x = x & 3	
|=	        x |= 3	    x = x | 3	
^=	        x ^= 3	    x = x ^ 3	
>>=	        x >>= 3 	x = x >> 3	
<<=	        x <<= 3	    x = x << 3	

Comparison Operators
Comparison operators are used to compare two values.

A list of all comparison operators:

Operator	Name	                    Example
==	        Equal to	                x == y	
!=	        Not equal	                x != y	
>	        Greater than	            x > y	
<	        Less than	                x < y	
>=	        Greater than or equal to	x >= y	
<=	        Less than or equal to	    x <= y	

Logical Operators
Logical operators are used to determine the logic between variables or values:

Operator	Name	        Description	                                                Example	
&& 	        Logical and	    Returns true if both statements are true	                x < 5 &&  x < 10	
|| 	        Logical or	    Returns true if one of the statements is true	            x < 5 || x < 4	
!	        Logical not	    Reverse the result, returns false if the result is true	    !(x < 5 && x < 10)	

Sizeof Operator
The memory size (in bytes) of a data type or a variable can be found with the sizeof operator:

Example
int myInt;
float myFloat;
double myDouble;
char myChar;

printf("%lu\n", sizeof(myInt));
printf("%lu\n", sizeof(myFloat));
printf("%lu\n", sizeof(myDouble));
printf("%lu\n", sizeof(myChar));
