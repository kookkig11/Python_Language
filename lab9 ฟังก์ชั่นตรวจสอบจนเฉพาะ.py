def check_prime(n) :
    if n%2==0 and n//2>1 :
        result = False
    elif n%3==0 and n//3>1 :
        result = False
    elif n%5==0 and n//5>1 :
        result = False
    elif n%7==0 and n//7>1 :
        result = False
    elif n%11==0 and n//11>1 :
        result = False 
    elif n%13==0 and n//13>1 :
        result = False
    else :
        result = True
    return result
        
n = int(input("Enter number: "))
if check_prime(n) :
    print(n,"is a prime number.")
else :
    print(n,"is not a prime number.")