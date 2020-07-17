secret = int(input("Enter secret code: "))
word = ""
while True:
    char = secret & 255 #ANDกับ255 #ได้เลข8bitสุดท้าย #แปลงเป็นchar
    if char == 0:
        break
    word = chr(char) + word #เก็บcharใส่word #เก็บไปเรื่อยๆ
    secret = secret >> 8 #shiftจน8bitหายไป
print("word: %s" % word)