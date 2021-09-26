from sys import stdin, stdout

n, q = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

for _ in range(q):
    left, right, x = map(int, stdin.readline().split())
    
    l = left - 1
    r = right - 1
    
    mid = 0
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            r -= 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    
    if arr[mid] < x:
        mid += 1

    stdout.write(f'{right - mid}\n')