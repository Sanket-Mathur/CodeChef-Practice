try:
    for _ in range(int(input())):
        N = int(input())
        C = 0
        while(N):
            if N >= 100:
                C += N//100
                N %= 100
            elif N >= 50:
                C += N//50
                N %= 50
            elif N >= 10:
                C += N//10
                N %= 10
            elif N >= 5:
                C += N//5
                N %= 5
            elif N >= 2:
                C += N//2
                N %= 2
            else:
                C += N//1
                N = 0
        print(C)
except:
    pass
