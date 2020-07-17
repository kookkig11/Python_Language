area = input()
a1 = area.split('x')
m = int(a1[1]) * [0]

ls = [] #ตัวเกม
for i in range(int(a1[0])):
    ls.append(m)
    i = i + 1
print(ls)
    
bomb = int(input())
lsPoint = [] #ตน.ระเบิด
i = 1
while i <= bomb:
    point = input()
    x = point.split(',')
    lsPoint.append(x)
    i = i + 1

j = 0
while j < bomb:
    ls[int(lsPoint[j][0])].insert(int(lsPoint[j][1]),'x')
    ls[int(lsPoint[j][0])].pop((int(lsPoint[j][1]))+1)
    j = j + 1
print(ls)
    