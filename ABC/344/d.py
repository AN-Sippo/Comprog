t = input()
n = int(input())
A = [list(input().split())for _ in range(n)]

INF = 10**10
dp = [[INF for _ in range(len(t)+1)] for _ in range(n)] 
for ni in range(n):
    dp[ni][0] = 0
for ni in range(n):
    for length in range(len(t)+1):
        dp[ni][length] = min(dp[ni - 1][length],dp[ni][length])
        for si in A[ni]:
            if len(si) > length or si != t[length - len(si):length]:
                continue 
            dp[ni][length] = min(dp[ni][length],dp[ni-1][length - len(si)] + 1)



ans = dp[n-1][len(t)]
if ans == INF:
    ans = -1
print(ans)

            
            

