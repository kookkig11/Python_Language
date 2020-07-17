num = input()
finddot = num.find('.')
changedot = num.replace('.','')
changeand = changedot.replace(',','')

if changeand.isdigit() != True :
    print("ERROR")
else :
    countand = num.count(',')
    countdot = num.count('.')
    i = 1
    if len(num[finddot+1:]) > 2 :
        print("ERROR")
    else :
        if countdot == 1 :
            if len(num[finddot+1:]) == 1 :
                if countand > 0 :
                    while True:
                        if num[(-4*i)-2] == ',' :
                            i = i + 1
                            x = num.replace(',','')
                            y = float(x)
                            print(y+1)
                        else:
                            i = i + 1
                            print("ERROR")
                            break
                else:
                    y = float(num)
                    print(y+1)
            elif len(num[finddot+1:]) == 2 :
                if countand > 0 :
                    while True:
                        if num[(-4*i)-3] == ',' :
                            i = i + 1
                            x = num.replace(',','')
                            y = float(x)
                            print(y+1)
                        else:
                            i = i + 1
                            print("ERROR")
                            break
                else:
                    y = float(num)
                    print(y+1)
        elif countdot == 0:
            if countand > 0 :
                while True:
                    if num[-4*i] == ',' :
                        i = i + 1
                        x = num.replace(',','')
                        y = int(x)
                        print(y+1)
                    else:
                        i = i + 1
                        print("ERROR")
                        break
            else:
                y = int(num)
                print(y+1)