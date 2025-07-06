# NearlyLuckyNumber
# Problem ID: 110A
# Rating: 800

S = input()
N = len(S)

count = 0
stat = False

for i in range(0,N):
	if S[i] == '4' or S[i] == '7':
		count += 1

if count == 4 or count == 7:
	print("YES")
else:
	print("NO")
