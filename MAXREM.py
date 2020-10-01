N = int(input())
L = sorted(set(map(int, input().split())), reverse=True)

print(L[1] if len(L)>1 else 0)
