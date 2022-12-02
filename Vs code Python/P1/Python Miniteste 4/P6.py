a = 2 * 2
b = 5
if (a + b < 10):
    while (b - a <= 1):
        c = (a / 2) + b
        b = b + 1
        a = a - 2
else:
    while (b - a > 1):
        c = b / 2 
        b = a + 1

print(a)
print(b)
print(c)
