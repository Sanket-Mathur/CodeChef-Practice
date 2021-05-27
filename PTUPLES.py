from sys import stdin, stdout

N = 10**6 + 2
prime = [False, False] + [True] * (N-2)
p = 2
while p*p <= N:
    if prime[p]:
        for mul in range(p*p, N, p):
            prime[mul] = False
    p += 1

result = {}
cnt = 0
for i in range(2,N):
    if prime[i] and prime[i-2]:
        cnt += 1 
    result[i] = cnt
    

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    stdout.write(f'{result[n]}\n')
