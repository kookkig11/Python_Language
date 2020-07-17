num = int(input())
a = 1
summ = 0
while a <= num :
    if num%a == 0 :
        b = num // a
        if summ == 0 :
            summ = a + b
        elif summ > (a+b) :
            summ = a + b
    a = a + 1
print("%d" %summ)