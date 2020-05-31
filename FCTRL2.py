T = int(input())
for t in range(T):
	X = int(input())
	fact = 1
	for i in range(1,X+1):
		fact *= i
	print(fact)