# SoldierAndBananas
# Problem ID: 546A
# Rating: 800

K,N,W = map(int,input().split(" "))

cost = K * (W)*(W+1)//2


if (cost - N < 0):
	print(0)
else:
	print(cost - N)