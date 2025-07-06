# YoungPhysicist
# Problem ID: 69A
# Rating: 1000

N = int(input())

F_x,F_y,F_z = 0,0,0

while (N > 0):
	X,Y,Z = map(int,input().split())

	F_x += X
	F_y += Y
	F_z += Z	

	N -= 1


if (F_x == 0) and (F_y == 0) and (F_z == 0): 
	print("YES",end="\n")
else:
	print("NO",end="\n")