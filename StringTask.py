# StringTask
# Problem ID: 118A
# Rating: 1000

S = input().lower()


for val in "aoyeui":
	S = S.replace(val, "")


new_S = ""

for val in S:
	new_S += "."+val



print(new_S)