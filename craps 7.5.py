first = int(input())
second = int(input())
while first > 6 or first < 1 or second > 6 or second < 1 :
    print("ERROR")
    first = int(input())
    second = int(input())
if first + second == 7 or first + second == 11 :
    print("1",first + second,"W")
elif first + second == 2 or first + second == 3 or first + second == 12 :
    print("1",first + second,"L")
else :
    i = 1
    while True :
        first_i = int(input())
        second_i = int(input())
        while first_i > 6 or first_i < 1 or second_i > 6 or second_i < 1 :
            print("ERROR")
            first_i = int(input())
            second_i = int(input())
        i = i + 1
        if first_i + second_i == 7 :
            print(i, first_i + second_i,"L")
            break
        elif first_i + second_i == first + second :
            print(i, first_i + second_i,"W")
            break