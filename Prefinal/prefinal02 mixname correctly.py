father = input()
mother = input()

s = ''
count1 = 1
for i in father:
    if i in 'aeiou':
        count1 += 1
    if count1 <= 2:
        s = s + i
cc = len(mother) - 1
boo = False

for i in mother:
    if i in 'aeiou':
        boo = True

if boo == True:
    t = 0
    while t < len(mother):
        if mother[t] in 'aeiou':
            index = t
            break
        t += 1
    count2 = 1
    s1 = ''
    while cc != index:
        s1 = s1 + mother[cc]
        cc -= 1
    ls = []
    cc1 = len(s1) - 1
    w = ''
    while cc1 != -1:
        w = w + s1[cc1]
        cc1 -= 1
else:
    w = mother
print(s + w)