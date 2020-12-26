from math import floor
for _ in range(int(input())):
    S = input()
    d = {}
    for i in S:
        if i not in d:
            d[i] = 1 
        else:
            d[i] += 1 
    singles = doubles = 0
    for i in d:
        doubles += d[i] // 2
        d[i] %= 2
        singles += d[i]
    if singles >= doubles+1:
        print(doubles)
    else:
        print(singles + floor(((doubles-singles) / 3) * 2))
