'''
Tipo Booleano

  - Operadores da álgebra booleana
     - AND
        - binário
	- Faz a conjunção de dois valores lógicos
        - Tabela-verdade:
		op1   | and | op2  | result
		TRUE  |     | TRUE | TRUE
 		TRUE  |     | FALSE| FALSE
		FALSE |     | TRUE | FALSE
		FALSE |     | FALSE| FALSE

     - OR
	 - binário
	 - Faz a disjunção de dois valores lógicos
		- verdadeiro quando ao menos um dos valores for verdadeiro
	- Tabela-verdade:
		op1   | or | op2  | result
		TRUE  |    | TRUE | TRUE
 		TRUE  |    | FALSE| TRUE
		FALSE |    | TRUE | TRUE
		FALSE |    | FALSE| FALSE

     - NOT
	- unário
	- inverte o valor lógico do operando
	- Tabela-verdade:
		not op1  | result
		    TRUE | FALSE
		    FALSE| TRUE
'''
from zipfile import ZIP_BZIP2


x0 = 2 > 1 and 3 > 1
x1 = 2 > 1 and 3 > 4
x2 = 2 > 3 and 3 > 1
x3 = 2 > 3 and 3 > 4
print(type(x0))
print(x0, x1, x2, x3)

z0 = 2 > 1 or 3 > 1
z1 = 2 > 1 or 3 > 4
z2 = 2 > 3 or 3 > 1
z3 = 2 > 3 or 3 > 4
print(type(z0))
print(z0, z1, z2, z3)

y0 = not 2 > 1  
y1 = not 2 > 3
print(type(y0))
print(y0, y1)
