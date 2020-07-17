c = int(input())
a = 0
i = 0
while a < c :
    b = a
    while b < c :
        if (c**2) == (a**2) + (b**2) :
            i = i + 1
        b = b + 1
    a = a + 1
print(i)