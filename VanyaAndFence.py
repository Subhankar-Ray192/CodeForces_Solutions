# VanyaAndFence
# Problem ID: 677A
# Rating: 800

N,H_M = map(int, input().split())
H_F = list(map(int, input().split()))

valid_width = 0

for val in H_F:
	if val <= H_M:
		valid_width += 1
	else:
		valid_width += 2

print(valid_width)
