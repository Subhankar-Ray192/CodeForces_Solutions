# BitPlusPlus
# Problem ID: 282A
# Rating: 800

import re

LC = int(input())

X = 0

psig = r"^\++|\++$"
nsig = r"^\-+|\-+$"


while (LC > 0):

	line = input()
	stat = re.search(psig, line)

	if (stat):
		X = X + 1
	
	stat = re.search(nsig, line)

	if (stat):
		X = X - 1
	

	LC = LC - 1


print()
print(X, end="\n")