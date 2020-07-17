def cutl(word) :
    return word[:word.find('=')].strip()
def cutr(word) :
    return word[word.find('=')+1:].strip()

space = 1
letter = ''

while True :
    word = input()
    if word == '-1' :
        break
    if len(cutl(word)) > space :
        space = len(cutl(word))
    letter = letter + cutl(word).rjust(space) + ' = ' + cutr(word) + '\\'

while len(letter) > 0 :
    l = cutl(letter[:letter.find('\\')])
    r = cutr(letter[:letter.find('\\')])
    print(l.rjust(space) + ' = ' + r)
    l = r = ''
    letter = letter[letter.find('\\')+1:]