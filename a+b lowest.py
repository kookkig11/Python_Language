n = int(input())
a = 0
summ = 0
while a < n :
    b = a
    while b < n :
        if n == a * b :
            summ = a + b
        b = b + 1
    a = a + 1
print(summ)