word = input()
move = int(input())
lenW = len(word)

if move > 0 :
    print(word[(lenW-move):] + word[:(lenW-move)])
elif move < 0 :
    print(word[(-move):lenW] + word[:(-move)])
else:
    print(word)
    
    
#word = input()
#move = int(input())

#if move > 0 or move < 0 :
#    print(word[(-move):] + word[:(-move)])
#else:
#    print(word)