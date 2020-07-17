word1 = input()
word2 = input()

lenWord = len(word1)

i = 0
count = 0
while i < lenWord :
    if word1[i] == word2[i] :
        count = count + 1
    i = i + 1

ls = []
i = 0
for x in word1:
    ls.append(x)
    y = ls.count(x)
    if y == 1 :
        i = i + 1
    else:
        ls.pop(i)

donels =''
for y in ls:
    donels = donels + y

count2 = 0
for z in donels :    
    if z in word2 :
        count2 = count2 + 1
        
print(count,end='')
print('-',end='')
print(count2)
