area = input()
a1 = area.split('x')
m = int(a1[1]) * [0]

ls = []
for i in range(int(a1[0])):
    ls.append(m)
    i = i + 1
print(ls)
    
bomb = int(input())
lsPoint = []
i = 1
while i <= bomb:
    point = input()
    b1 = point.split(',')
    lsPoint.append(b1)
    i = i + 1

j = 0
while j < bomb:
    x = int(lsPoint[j][0])
    y = int(lsPoint[j][1])
    ls[x].insert(y,'*')
    ls[x].pop(y+1)
    j = j + 1

print(ls)