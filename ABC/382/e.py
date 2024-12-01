n, x = map(int, input().split())
plst = list(map(lambda x: int(x) / 100, input().split()))

prob_map = [
    [0 for _ in range(n + 1)] for _ in range(n + 1)
]  # dp[i][j]：前からi番目までにちょうどj枚レアカードが入っている確率
prob_map[0][0] = 1
for i in range(1, n + 1):
    for j in range(n + 1):
        if j == 0:
            prob_map[i][j] = prob_map[i - 1][j] * (1 - plst[i - 1])
            continue
        prob_map[i][j] = (
            prob_map[i - 1][j] * (1 - plst[i - 1])
            + prob_map[i - 1][j - 1] * plst[i - 1]
        )

prob_map = prob_map[n]
dp = [
    0 for _ in range(x + 1)
]  # dp[i]:ちょうどi枚のレアカードを手に入れるまでのパック数期待値

dp[0] = 0

for i in range(1, x + 1):
    for j in range(1, min(i + 1, n + 1)):
        dp[i] += dp[i - j] * prob_map[j]
    dp[i] += 1
    dp[i] /= 1 - prob_map[0]

print(dp[x])
