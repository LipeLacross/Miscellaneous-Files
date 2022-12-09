b = 7
a = 3
while (b > a):
    c = b - 2
    print(c)
    a = a + 1
    b = b - 1

print(a,b,c)

a = 5

while (a > 0):
    if (a % 3 == 0):
        b = a + 1
    else:
        b = 3 * a
    c = a + b
    a = a - 2

print(a, b, c)