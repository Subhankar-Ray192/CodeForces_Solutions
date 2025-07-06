# HelpfulMaths
# Problem ID: 339A
# Rating: 800

EXP = sorted(list(map(int,input().split("+"))))

res = ""

for val in EXP:
	res = res + str(val) + "+"

L = len(res)

print(res[0:L-1],end="\n")