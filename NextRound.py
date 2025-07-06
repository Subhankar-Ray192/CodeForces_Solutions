# NextRound
# Problem ID: 158A
# Rating: 800

n, k = map(int, input().split())
scores = list(map(int, input().split()))

# Score of the k-th place participant
threshold = scores[k - 1]

# Count how many scores are >= threshold and > 0
advancers = sum(1 for score in scores if score >= threshold and score > 0)

print(advancers)


