from itertools import permutations

N, M = list(map(int, input().split()))
edges = []
for _ in range(M):
    ui, vi, ti = map(int, input().split())
    edges.append((ui - 1, vi - 1, ti))

Q = int(input())

# warshallfloyd
INF = 10**13 - 1
dp = [[INF for _ in range(N)] for _ in range(N)]
# dp[k][i][j]   i->jの最短コストで、iとj以外は0-k頂点のみを通る。

for ui, vi, ti in edges:
    dp[ui][vi] = min(dp[ui][vi], ti)
    dp[vi][ui] = min(dp[vi][ui], ti)

for i in range(N):
    dp[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


costs = dp
for _ in range(Q):
    ans = INF
    ki = int(input())
    blst = list(map(int, input().split()))
    for edge_nums in permutations(blst):
        for bit in range(1 << ki):
            before = 0
            tmp = 0
            for idx, edge_num in enumerate(edge_nums):
                ui, vi, ti = edges[edge_num - 1]
                start, end = (ui, vi) if (bit >> idx) & 1 else (vi, ui)
                tmp += costs[before][start]
                tmp += ti
                before = end
            tmp += costs[before][N - 1]
            ans = min(ans, tmp)

    print(ans)
