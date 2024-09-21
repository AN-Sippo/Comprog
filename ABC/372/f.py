n, m, k = map(int, input().split())

edges = []

for _ in range(m):
    edges.append(list(map(lambda x: int(x) - 1, input().split())))

dp = [1 for _ in range(n)]
for ki in range(k):
    for xi, yi in edges:
        dp[yi] += dp[xi]

print(sum(dp) % 998244353)
