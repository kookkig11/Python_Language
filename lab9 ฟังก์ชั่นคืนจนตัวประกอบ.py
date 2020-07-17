def factor_count(n):
    a = 1
    count = 0
    while a <= n :
        if n%a == 0 :
            count = count + 1
        a = a + 1
    return count

n = int(input("Enter n: "))
c = factor_count(n)
print(c)