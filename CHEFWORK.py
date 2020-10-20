N = int(input())
c = list(map(int, input().split()))
t = list(map(int, input().split()))

t1, t2, t3 = [], [], []
for i in range(N):
    if t[i] == 1:
        t1.append(c[i])
    elif t[i] == 2:
        t2.append(c[i])
    else:
        t3.append(c[i])

if t1 and t2 and t3:
    m3 = min(t3) 
    m12 = min(t1) + min(t2) 
    print(m3 if m3<=m12 else m12)
elif t3:
    print(min(t3))
else:
    print(min(t1) + min(t2))
    
