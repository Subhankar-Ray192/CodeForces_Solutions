# StonesOnTheTable
# Problem ID: 266A
# Rating: 800

N = int(input())
balls = input()

count = 0

for val in range(0,N-1):
	if (balls[val] == balls[val+1]):
		count += 1

print(count,end="\n")