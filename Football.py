# Football
# Problem ID: 96A
# Rating: 900

S = list(map(int,list(input())))

N = len(S)
count = 0

for i in range(0,N-1):
	if (S[i] == 1 and S[i+1] == 1) or (S[i] == 0 and S[i+1] == 0):
		count += 1
	else:
		count = 0

	if count == 6:
		break


if count == 6:
	print("YES",end="\n")
else:
	print("NO",end="\n")