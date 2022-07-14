a = 10
b = 22 
while (b - a > 4):
    c = b - (2 * a)
    if (c > 0):
        d = c + 1
    else:
        d = c + 5
    a = a + 3
    b = b - 2

print(a)
print(b)
print(c)
print(d)