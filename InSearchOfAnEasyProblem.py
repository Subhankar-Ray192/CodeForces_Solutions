# InSearchOfAnEasyProblem
# Problem ID: 1030A
# Rating: 800

N = int(input())
V = list(map(int,input().split()))

stat = 1

for val in V:
	stat = stat and not val
	
	if not stat:
		break

if stat:
	print("EASY")
else:
	print("HARD")