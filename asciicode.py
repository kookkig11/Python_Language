secret = int(input("Enter secret code: "))
word = ""
while True:
    char = secret & 255 #AND�Ѻ255 #���Ţ8bit�ش���� #�ŧ��char
    if char == 0:
        break
    word = chr(char) + word #��char���word #����������
    secret = secret >> 8 #shift��8bit����
print("word: %s" % word)