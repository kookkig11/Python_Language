a = int(input("How many TVs? "))
b = int(input("How many DVD players? "))
c = int(input("How many Audio Systems? "))
total = a*6000 + b*1500 + c*3000
print("Total price is %.2f baht." % total)
if total >= 24000 :
    print("You've got a discount of %.2f baht." %(total*0.2))
    print("Your payment is %.2f baht. Thank you!" %(total*0.8))
else :
    print("Your payment is %.2f baht. Thank you!" % total)