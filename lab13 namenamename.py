def namelist(ls):
    s = ''
    for i in ls:
        s = s + i + ', '
    s = s.strip(', ')
    print(s)
    s1 = ''
    for i in range(len(s)-1,-1,-1):
        s1 = s1 + s[i]
    print(s1)
    s1 = s1.replace(' ,',' & ',1)
    print(s1)
    s2 = ''
    for i in range(len(s1)-1,-1,-1):
        s2 = s2 + s1[i]
    return s2


import ast
names = ast.literal_eval(input())
print( namelist(names) )