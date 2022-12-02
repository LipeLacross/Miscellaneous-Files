b = 5
c = 1
a = b + c
d = b - c
while (b > 1):
    d = b - c + 1
    while (d > 1):
        if (d >= 3):
            a = c + 1
        else:
            a = a + 4
        d = d - 2
    b = b - 2
c = a + b + d

print(a)
print(b)
print(c)
print(d)