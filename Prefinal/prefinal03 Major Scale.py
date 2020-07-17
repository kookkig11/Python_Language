note = input()
num = int(input())
ls = note.split(',')

a = []
i = 0
for x in ls:
    a.append(x)
    y = a.count(x)
    if y == 1 :
        i = i + 1
    else:
        a.pop(i)

j = 0
if num > len(a):
    while j <= num//7:
        x = num-(7*j)
        j = j + 1
    print(a[x-1])
else:
    print(a[num-1])