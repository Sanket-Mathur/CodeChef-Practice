total = 0
for i in input():
    if i == 'D':
        total += 238
    elif i == 'T':
        total += 244
    elif i == 'M':
        total += 138
    elif i == 'B':
        total += 279
    elif i == 'C':
        total += 186

print(total // 50)
total %= 50
print(total // 5)
total %= 5 
print(total * 2)
