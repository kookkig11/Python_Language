n = int(input())
lsNum = []

i = 1
while i <= n :
    num = int(input())
    lsNum.append(num)
    i = i + 1   
lsNum.sort()

lsDiff = []
j = 0
for j in range(n-1) :
    x = lsNum[j+1] - lsNum[j]
    lsDiff.append(x)
    j = j + 1
print(lsDiff)

ls2 = []
n = 0
while True:
    div = abs(lsNum[n] - lsNum[n+1])
    ls2.append(div)
    n += 2
    if n == len(lsNum)-2:
        break
print(ls2)