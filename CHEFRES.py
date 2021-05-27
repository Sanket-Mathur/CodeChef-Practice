from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    rest = []
    for i in range(n):
        rest.append(tuple(map(int, stdin.readline().split())))
    
    rest.sort(key = lambda x:x[0])
    
    for i in range(m):
        p = int(stdin.readline())
        
        low,high = 0, n-1
        while low <= high:
            mid = (low + high) // 2
            if rest[mid][0] == p:
                break
            elif rest[mid][0] > p:
                high = mid-1
            else:
                low = mid+1 

        if rest[mid][0] <= p and rest[mid][1] > p:
            stdout.write('0\n')
        elif rest[mid][0] > p:
            if mid == 0 or rest[mid-1][1] <= p:
                stdout.write(f'{rest[mid][0] - p}\n')
            else:
                stdout.write('0\n')
        elif mid == n-1:
            stdout.write('-1\n')
        else:
            stdout.write(f'{rest[mid+1][0] - p}\n')
