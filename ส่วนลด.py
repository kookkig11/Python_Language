#input
amount_buy = float(input("Enter buying amount: "))
#process
if amount_buy>=1000 and amount_buy<3000 :
    amount_due == amount_buy * 0.9
elif amount_buy>=3000 :
    amount_due == amount_buy * 0.85
else:
    amount_due == amount_buy
#output
print ('Amount due after discount is %.2f baht.' % amount_due)