# Word
# Problem ID: 59A
# Rating: 800

S = list(input())

stat_cap = 0
stat_ncap = 0

for val in S:
	if (ord(val) <= 91) and (ord(val) >= 65):
		stat_cap += 1
	else:
		stat_ncap += 1

S = ''.join(S)

if (stat_ncap >= stat_cap):
	S = S.lower() 
else:
	S = S.upper()

print(S)