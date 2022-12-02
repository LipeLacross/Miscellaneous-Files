def find(item, lista):
    for x in lista:
        if x == item:
            return True
    return False

number = 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
    
print(find(number, numbers))