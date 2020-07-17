word = input()
w1 = word.lower()

count = 0
i = 0
for x in w1:
    a = ord(x)
    if count < a :
        count = a
        i = i + 1
    else:
        break

print(i)