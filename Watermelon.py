# Watermelon
# Problem ID: 4A
# Rating: 800

g_wt = int(input())
stat = True

for i in range(2,g_wt-1,2):
	if g_wt % i == 0:
		print("YES", end="\n")
		stat = False
		break
if (stat):
	print("NO", end="\n")

