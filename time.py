s1 = int(input("Enter your exercise time 1: "))
s2 = int(input("Enter your exercise time 2: "))
ex = s1+s2
hours = ex//3600
minutes = (ex%3600)//60
seconds = (ex%3600)%60
print ("It is", hours ,"hours", minutes ,"minutes", seconds ,"seconds.")