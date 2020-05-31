T = int(input())
for t in range(T):
	N = int(input())
	L = list(map(int, input().split()))
	l = [str(L[0])]
	F = list()
	for i in range(1,N):
		if(L[i-1] + 1 == L[i]):
			l.append(str(L[i]))
		elif(len(l)<3):
			F.extend(l)
			l = [str(L[i])]
		else:
			F.append(str(l[0])+"..."+str(l[-1]))
			l = [str(L[i])]
	if(len(l)<3):
		F.extend(l)
	else:
		F.append(str(l[0])+"..."+str(l[-1]))
	print(*F, sep=',')
	print('')
