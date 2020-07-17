import math
bullet = int(input())
zombie = input()
ls = zombie.split(' ')

times = 0
lsAns = []
for x in ls :
    times = times + math.ceil(int(x)/bullet)
    lsAns.append(times)

print(times)

for y in lsAns :
    print(y, end=' ')