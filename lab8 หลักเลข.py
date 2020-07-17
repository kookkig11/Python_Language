def digit(n) :
    digit = n%10
    return digit
def tens(n) :
    ten = (n//10)%10
    return ten
def hundreds(n) :
    hundred = (n//100)%10
    return hundred
def thousands(n) :
    thousand = n//1000
    return thousand
def sum_digits(n) :
    summ = n%10 + (n//10)%10 + (n//100)%10 + n//1000
    return summ

n = int(input("Enter a number (0 to 9999): "))
print("Digit place is %d." %digit(n))
print("Tens place is %d." %tens(n))
print("Hundreds place is %d." %hundreds(n))
print("Thousands place is %d." %thousands(n))
print("Sum of all digits is %d." %sum_digits(n))