i = 0
sum = 0
while True :
    x = input()
    # check non-input ?
    if x == "" :
        break
    else :
        num = float(x)    
        # loop start and set default value
        if i == 0 :
            max = num
            min = num
        # num is positive integer
        if num >= 0 :
            if num > max :
                max = num    
            if num < min :
                min = num
        sum += num
    # count loop
    i = i + 1

# average
avg = sum / i
# output
print("%.2f %.2f" %(max, min))
print("%.2f %.2f" %(sum, avg))