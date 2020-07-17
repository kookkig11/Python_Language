card = input()
lsCard = card.split(' ')

J = 10
Q = 10
K = 10

ls = []
for x in lsCard:
    if x not in 'AJQK':
        ls.append(x)
        
summ = 0
for y in ls:
    summ = summ + int(y)
    
for z in lsCard:
    if z in 'A' :
        if summ <= 10 :
            summ = summ + 11
        elif summ > 10:
            summ = summ + 1
print(summ)