def nb_year(p0,percent,aug,p) :
    day = 0
    num = p0
    while p0 < p :
        num = (num*2) * (percent/100) + aug
        day = day + 1
        if p0 >= p :
            break
    return day

p0 = int(input())
percent = float(input())
aug = int(input())
p = int(input())

print(nb_year(p0,percent,aug,p))
