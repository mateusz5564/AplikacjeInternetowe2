x = []
y = 1000000 #<-----LICZBA POCZĄTKOWA
x.append(y)

while (y > 1):
    if(y % 2 == 0):
        y = int(y / 2)
        x.append(y)
    else:
        y = 3*y + 1
        x.append(y)

print(*x, sep=" -> " )
print('Liczba elementów: ', len(x))