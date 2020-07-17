word = input()
space = word.strip()
code = space.split(',')
a = ''
for x in code:
    a = a + '"'
    y = x.strip()
    a = a + y
    a = a + '"'
    a = a + ','
b = a.rstrip(',')
print(b)