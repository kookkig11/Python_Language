word = input()
w1 = word.lower()
w2 = w1.title()
w3 = w2.replace('For','for')
w4 = w3.replace('And','and')
w5 = w4.replace('With','with')
letter = w5.replace('Of','of')
print(letter)