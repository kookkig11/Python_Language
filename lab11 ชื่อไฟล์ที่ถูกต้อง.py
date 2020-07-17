file = input()
f1 = file.replace('\\','_')
f2 = f1.replace('/','_')
f3 = f2.replace('*','_')
f4 = f3.replace(':','_')
f5 = f4.replace('|','_')
f6 = f5.replace('"','_')
f7 = f6.replace('<','_')
f8 = f7.replace('>','_')
f9 = f8.replace(' ','_')
countdot = f9.count('.')
f10 = f9.replace('.','_',countdot-1)
lastdot = f10.find('.')

if countdot > 0 :
    if len(f10[:lastdot]) < 15:
        print(f10[:lastdot] + f10[lastdot:lastdot+4])    
    else :
        print(f10[:15] + f10[lastdot:lastdot+4])
else:
    print(f10[:15])