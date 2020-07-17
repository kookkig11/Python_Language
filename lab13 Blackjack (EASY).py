num = int(input())
ans = []

card = ["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]

dex = ''
ls5C = []
lsm = []
if num >= 1 and num <= 100:
    for i in range(num):
        x = input()
        ls5C = x.split()
        
        for y in ls5C:
            dex = dex + y + ' '
        dex = dex.replace('A','1')
        dex = dex.replace('J','10')
        dex = dex.replace('K','10')
        dex = dex.replace('Q','10')
        lsm = dex.split()
        
        j = 0
        n = 0
        summ = 0
        while n < num:
            while j < 5 :
                for z in lsm[j+(n*5)]:
                    z = int(z)
                    print(z)
                    summ = summ + z
                    print(summ)
                    if summ >= 16:
                        break
                j = j + 1
            n = n + 1 
        ans.append(summ)

for i in ans:
    if  i > 21:
        print('busted')
    else:
        print(i)