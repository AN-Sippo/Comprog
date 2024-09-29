# from sys import setrecursionlimit

# setrecursionlimit(200000)

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    ui, vi, wi = map(int, input().split())
    ui -= 1
    vi -= 1
    edges[ui].append([vi, wi])
    edges[vi].append([ui, -wi])

ans = [-1 for _ in range(n)]
visited = [False for _ in range(n)]


stack = [[i, 0] for i in range(n)]
while stack:
    ui, ansi = stack.pop()
    if visited[ui]:
        continue
    visited[ui] = True
    ans[ui] = ansi
    for vi, wi in edges[ui]:
        if not visited[vi]:
            stack.append([vi, ansi + wi])

# def dfs(current_idx, current_weight):
#     if visited[current_idx]:
#         return
#     visited[current_idx] = True
#     ans[current_idx] = current_weight
#     for vi, wi in edges[current_idx]:
#         if visited[vi]:
#             continue
#         dfs(vi, current_weight + wi)


# for i in range(n):
#     if visited[i]:
#         continue
#     dfs(i, 0)
print(*ans)
