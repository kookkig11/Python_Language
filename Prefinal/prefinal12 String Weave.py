word = input()

x = ''
i = 0
while i < len(word)//2:
    x = x + word[i]
    x = x + word[(len(word)-1) - i]
    i = i + 1

if len(word)%2 == 0:
    print(x)
else:
    print(x + word[len(word)//2])