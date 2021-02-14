for _ in range(int(input())):
    A, B = map(int, input().split())
    binA = bin(A)[2:]
    binB = bin(B)[2:]
    i = 0
    k = min(len(binA), len(binB))
    while i < k and binA[i] == binB[i]:
        i += 1 
    print(len(binB) + len(binA) - (2 * i))
