# WayTooLongWords
# Problem ID: 71A
# Rating: 800

N = int(input())
res = ""

abr_list = []

while (N > 0):
	wrd = input()
	L = len(wrd)

	if L > 10:
		res = res + wrd[0] + str(len(wrd[1:L-2]) + 1) +wrd[L-1]
		abr_list.append(res)
	else:
		abr_list.append(wrd)

	N = N -1
	res = ""

print()
for abr in abr_list:
	print(abr, end="\n")

