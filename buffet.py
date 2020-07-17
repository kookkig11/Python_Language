a = input("Enter your buffet choice: ")
if a=='Japanese' :
    b = 1000
    w = input("Is today Wednesday (yes/no)? ")
    if w=='yes':
        c = b*0.85
    elif w=='no' :
        c = b
    print ("Your payment is %.2f Baht." % c)    
elif a=='Korean' :
    b = 1500
    w = input("Is today Wednesday (yes/no)? ")
    if w=='yes':
        c = b*0.85
    elif w=='no' :
        c = b
    print ("Your payment is %.2f Baht." % c)    
else :
    print ("Sorry, there is no %s buffet." % a)