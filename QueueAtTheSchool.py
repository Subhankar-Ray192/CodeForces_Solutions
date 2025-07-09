# QueueAtTheSchool
# Problem ID: 266B
# Rating: 800

N,T = map(int,input().split())
S = list(input())

while (T > 0):
	
	new_S = S.copy()
	i = 0

	while (i < N-1):
		if S[i] == 'B' and S[i+1] == 'G':
			new_S[i],new_S[i+1] ='G','B'
			i = i + 2
		else:
			i = i + 1

	S = new_S
	T -= 1

print(''.join(S))