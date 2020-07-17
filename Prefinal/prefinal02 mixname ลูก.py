father = input()
mother = input()

lsF = []
for x in father:
    if x in 'aeiou':
        lsF.append(x)
if len(lsF) == 1:
    a = father
elif len(lsF) == 0:
    a = father
else:
    findAlF = father.find(lsF[1])
    a = father[:findAlF]

lsM = []
for y in mother:
    if y in 'aeiou':
        lsM.append(y)
if len(lsM) == 0 :
    b = mother
elif len(lsM) > 0 :
    findAlM = mother.find(lsM[0])
    b = mother[(findAlM+1):]    

print(a + b)

    