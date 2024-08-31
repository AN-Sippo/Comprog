n = int(input())
alst = list(map(int, input().split()))

dp = [[0, 0] for _ in range(n)]  # i回目が終わった時に奇数,偶数
dp[0][0] = alst[0]
for i, ai in enumerate(alst):
    if i == 0:
        continue
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + ai)
    dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + ai * 2)

print(max(dp[i]))
