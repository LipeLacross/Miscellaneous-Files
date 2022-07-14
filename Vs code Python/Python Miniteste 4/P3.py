a = 4
b = a * a * a 
c = b / a 
if (c > a): 
    while (b / a > 1):
        c = c - a 
        b = b / 2 
else:
    c = a + c

print(a)
print(b)
print(c)