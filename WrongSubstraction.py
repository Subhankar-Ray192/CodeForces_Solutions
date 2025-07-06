# WrongSubstraction
# Problem ID: 977A
# Rating: 800

N,K=map(int,input().split())

while (K > 0):
	
	L = N % 10
	if (L == 0):
		N = N//10
	else:
		N -= 1

	K -= 1

print(N, end="\n")