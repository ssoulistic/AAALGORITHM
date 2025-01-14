input = open("sample.txt", 'r').readline
# import sys
# input=sys.stdin.readline
N = int(input())
weights = list(map(int, input().split()))
T = int(input())
balls = list(map(int, input().split()))

max_weight = sum(weights)
dp = [set() for _ in range(N+1)]
dp[0].add(0)

for i in range(1, N+1):
    weight = weights[i-1]
    for w in dp[i-1]:
        dp[i].add(w)
        dp[i].add(w + weight)
        dp[i].add(abs(w - weight))

results = []
for b in balls:
    if b in dp[N]:
        results.append("Y")
    else:
        results.append("N")
print(dp)
print(" ".join(results))
