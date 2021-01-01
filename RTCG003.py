S1 = input()
S2 = input()

count = 0
for i in range(min(len(S1),len(S2))):
    if S1[i] != S2[i]:
        count += 1
print(count)
