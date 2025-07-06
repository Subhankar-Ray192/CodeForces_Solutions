# WordCapitalization
# Problem ID: 281A
# Rating: 800

S  = input()


if ((ord(S[0]) >= 65) and (ord(S[0]) <= 91)):
	res = S[0] + S[1:]
else:
	res = chr(ord(S[0])-32) + S[1:]

print(res)