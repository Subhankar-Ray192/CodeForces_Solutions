# Tram
# Problem ID: 116A
# Rating: 800

N = int(input())

max_cap = float('-inf')
curr_cap = 0

for i in range(0,N):
	A,B = map(int,input().split())
	
	curr_cap += (B - A)
	
	if (max_cap < curr_cap):
		max_cap = curr_cap

print(max_cap)