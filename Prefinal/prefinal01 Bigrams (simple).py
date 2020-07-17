word = input()
w1 = word.lower()
w2 = w1.replace(' ','')
ls = []
ls1 = []
for x in range(len(w2)-1):
    y = x + 2
    ls.append(w2[x:y])
ls.sort()
for x in ls:
    if x not in ls1:
        print(x)
    ls1.append(x)