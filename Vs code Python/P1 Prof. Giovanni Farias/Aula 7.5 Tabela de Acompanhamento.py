a = 20
b = 5
if (a - b > 10):
    c = a + 2
    b = b + 3
else:
    c = a - 1
    b = c - 1
    a = b - 1
print(a)

'''
TABELA DE ACOMPANHAMENTO
	a	b	c	tela
	20
	20	5
	20	5	22
	20	8	22
	20	8	22	20
'''
a = 0
b = 5
c = a + b
print(c)
if (a / b > 0):
    c = a + b 
    a = b + c
    print(a)
elif (a/b == 0):
   a = b
   b = c
   c = a * b
   print(b) 
else:
    c = a - 1
    b = c - 1
    a = b - 1
    print(c)
c = a + b
print(c)

'''
TABELA DE ACOMPANHAMENTO
	a	b	c	tela
	0
	0	5
	0	5	5
	0	5	5	5
	5	5	5	5
	5	5	5	5
	5	5	25	5
	5	5	25	5
	5	5	10	5
	5	5	10	10
'''