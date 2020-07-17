l = int(input("Enter level pokemon: "))
ball = input("Enter level pokeball: ")
d = int(input("Enter distance: "))
if l>=0 and l<40 :
    if ball=='h' or ball=='H' :
        x = 0.01
    elif ball=='m' or ball=='M' :
        x = 0.03
    elif ball=='l' or ball=='L' :
        x = 0.05
elif l>=41 and l<60 :
    if ball=='h' or ball=='H' :
        x = 0.01
    elif ball=='m' or ball=='M' :
        x = 0.05
    elif ball=='l' or ball=='L' :
        x = 0.03
elif l>=61 and l<=100 :
    if ball=='h' or ball=='H' :
        x = 0.01
    elif ball=='m' or ball=='M' :
        x = 0.08
    elif ball=='l' or ball=='L' :
        x = 0.1
s = 100 - (l * d * x)
print ("%.2f percent." % s)