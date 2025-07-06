# BearAndBigBrother
# Problem ID: 791A
# Rating: 800

A,B = map(int, input().split(" "))

fA,fB = 3,2

Y = 0

while (A <= B):

	A = fA*A
	B = fB*B

	Y = Y + 1

print(Y)