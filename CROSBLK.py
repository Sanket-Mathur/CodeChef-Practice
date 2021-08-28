from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    L = list(map(int, stdin.readline().split()))
    
    if (L[0] < max(L)):
        stdout.write('-1\n')
        continue
    
    stack = []
    for i in range(1, N):
        if len(stack) == 0 or L[i] < stack[-1]:
            stack.append(L[i])
        else:
            while len(stack) > 0 and stack[-1] <= L[i]:
                stack.pop()
            stack.append(L[i])
    
    stdout.write(f'{len(stack)}\n')