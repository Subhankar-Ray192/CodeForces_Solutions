# ChatRoom
# Problem ID: 58A
# Rating: 1000

s = input()
target = "hello"
j = 0

for c in s:
    if c == target[j]:
        j += 1
        if j == len(target):
            break

if j == len(target):
    print("YES")
else:
    print("NO")

