a,b = map(int, input().split())
y = abs(a-b)
if(y % 10 == 9):
    y -= 1
else:
    y += 1
print(y)