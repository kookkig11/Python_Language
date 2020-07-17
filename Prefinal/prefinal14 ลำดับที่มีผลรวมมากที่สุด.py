ls = []
while True:
    num = int(input())
    if num == 0 :
        break
    else:
        ls.append(num)

lsSum = []
summ = 0
i = 0
j = 0
while j < len(ls):
    i = j
    j = j + 1
    while i < len(ls):
        summ = summ + ls[i]
        lsSum.append(summ)
        i = i + 1
        if i >= len(ls):
            summ = 0

print(max(lsSum))