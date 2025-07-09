# BeautifulYear
# Problem ID: 271A
# Rating: 800

Y1 = int(input())


def isBeautifulYear(Y1):
	dict = {key: 0 for key in str(Y1)}

	for val in str(Y1):
		dict[val] += 1

		if dict[val] > 1:
			return True

	return False
	

X1 = Y1 + 1

while (isBeautifulYear(X1)):
	
	X1 += 1
	


print(X1)


	