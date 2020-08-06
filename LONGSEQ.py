try:
    for _ in range(int(input())):
        S = input()
        print("Yes" if S.count('1') == 1 or S.count('0') == 1 else "No")
except:
    pass
