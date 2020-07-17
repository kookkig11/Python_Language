letter = input()
l_nospace = letter.replace(' ','')
code = input()
word = input()

ls = []
i = 0
for x in l_nospace :
    ls.append(x)
    count = ls.count(x)
    if count == 1 :
        i = i + 1
    else:
        ls.pop(i)

doneletter = ''        
for y in ls :
    doneletter = doneletter + y

for z in word :
    if z in code:
        a = code.find(z)
        print(doneletter[a], end='')
    else:
        print(z, end='')