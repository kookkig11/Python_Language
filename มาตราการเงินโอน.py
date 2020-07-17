a = int(input("Enter your age: "))
b = int(input("Enter your net income: "))
if a>=15 and a<=60 :
    if b>=1 and b<=30000 :
        print("Your negative income tax is %.2f Baht." %(b*0.2))
    elif b>30000 and b<=79999 :
        print("Your negative income tax is %.2f Baht." %((80000-b)*0.12))
    else :
        print ("Invalid income.")
else:
    print ("Invalid age.")