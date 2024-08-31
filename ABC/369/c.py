n = int(input())
alst = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()
elif n == 2:
    print(3)
    exit()


dp = [1 for _ in range(n)]  # dp[i]:iを終端（含む）とした等差数列の数
dp[1] = 2
for i in range(2, n):
    dp[i] += 1
    if alst[i] - alst[i - 1] == alst[i - 1] - alst[i - 2]:
        dp[i] += dp[i - 1] - 1

print(sum(dp))
