cnt = curr = 0
input()
for i in map(int, input().split()):
    if i != 0:
        curr += 1 
    else:
        if curr > cnt:
            cnt = curr
        curr = 0
if curr > cnt:
    cnt = curr
print(cnt)
