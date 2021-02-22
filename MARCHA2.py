from sys import stdin, stdout

answer = []
for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    L = [int(x) for x in stdin.readline().split()]
    nextMax = 1.0
    flag = True
    for i in range(N-1):
        if L[i] > nextMax:
            flag = False
            break
        else:
            nextMax = (nextMax - L[i]) * 2
    answer.append('Yes' if flag and nextMax == L[-1] else 'No')

print(*answer, sep='\n')
