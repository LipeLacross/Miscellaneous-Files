a = 20
b = 8
c = a - b
while (c > 1):
    a = a - 4
    b = b +1
    if (b > 12):
        c = c - 1 
    elif (a < 6):
        c = c - 2 
    else:
        c = c -3 
b = b / a 
a = (c + b) / a

print(a)
print(b)
print(c)
