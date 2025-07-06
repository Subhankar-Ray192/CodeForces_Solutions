# AntonAndDanik
# Problem ID: 734A
# Rating: 800

N = int(input())
S = input()

count = 0

for win in S:
	if win == 'A':
		count+=1
	else:
		count+=-1


if count < 0:
	print("Danik")
elif count == 0:
	print("Friendship")
else:
	print("Anton")