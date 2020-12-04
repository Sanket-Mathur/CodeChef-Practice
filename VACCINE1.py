D1, V1, D2, V2, P = map(int, input().split())
day = 0 
while P > 0:
    day += 1
    if day >= D1:
        P -= V1 
    if day >= D2:
        P -= V2 
print(day)
