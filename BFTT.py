for _ in range(int(input())):
    N = int(input()) + 1
    while list(str(N)).count('3') < 3:
        N += 1 
    print(N)
