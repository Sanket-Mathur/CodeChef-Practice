for _ in range(int(input())):
    N = int(input())
    words = input().split()
    w = dict()
    for i in words:
        b = i[1:]
        if b in w:
            w[b].append(i[0])
        else:
            w[b] = [i[0]]
    count = 0
    firsts = list(w.values())
    for i in range(len(firsts)-1):
        for j in range(i+1, len(firsts)):
            t = len(set(firsts[i] + firsts[j]))
            count += 2 * (t - len(firsts[i])) * (t - len(firsts[j]))
    print(count)
