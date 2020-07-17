#input
inc = float(input())
ex = float(input())
#output
print ("1234567890"*3)
print ("%-14s %+.2f bahts" % ("Total Income", inc))
print ("%-15s %.2f bahts" % ("Expense", ex))
print ("%-13s %08.2f bahts" % ("Profit", inc+ex))