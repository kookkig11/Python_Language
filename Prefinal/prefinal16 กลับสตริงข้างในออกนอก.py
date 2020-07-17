word = input()

a = ''
b = ''

i = ( len(word)//2 ) - 1
while i >= 0 :
    a = a + word[i]
    i = i - 1
    
if len(word)%2 == 0:
    j = len(word) - 1
    while j >= ( len(word)//2 ) :
        b = b + word[j]
        j = j - 1
    print(a + b)
else:
    j = len(word) - 1
    while j > ( len(word)//2 ) :
        b = b + word[j]
        j = j - 1
    print(a + word[len(word)//2] + b)    

