# Team
# Problem ID: 231A
# Rating: 800

N = int(input())

sol_prb = 0

while (N > 0):

	stat = sum(map(int,input().split(" ")))

	if (stat >= 2):
		sol_prb = sol_prb + 1

	N = N - 1

print()
print(sol_prb, end="\n")