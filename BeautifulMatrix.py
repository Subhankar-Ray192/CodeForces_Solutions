# BeautifulMatrix
# Problem ID: 263A
# Rating: 800

N = 5

R = 1

stat = True

while (N > 0):
	line = list(map(int,input().split(" ")))
	
	C = 1

	for val in line:
		if (val == 1):
			stat = False
			break

		C = C + 1

	if (not stat):
		break	

	R = R + 1	

	N = N - 1


R1 = 3
C1 = 3

print((abs(R1 - R) + abs(C1 - C)),end="\n")