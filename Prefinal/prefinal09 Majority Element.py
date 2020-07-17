num = int(input())

lsAl = []
for i in range(num):
    alpha = input()
    lsAl.append(alpha)

lsCount = []
for x in lsAl:
    y = lsAl.count(x)
    lsCount.append(y)

j = 0
for a in lsCount:
    if lsCount[j] == max(lsCount):
        break
    j = j + 1
    
if max(lsCount) > (num//2):
    print(lsAl[j])
else:
    print(0)