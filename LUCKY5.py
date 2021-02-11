for _ in range(int(input())):
    N = input().strip()
    print(len(N) - N.count('4') - N.count('7'))
