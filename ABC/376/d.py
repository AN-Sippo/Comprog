from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n)]

for _ in range(m):
    ai, bi = map(lambda x: int(x) - 1, input().split())
    edges[ai].append(bi)

queue = deque()
visited = [0 for _ in range(n)]
visited[0] = 1
for next in edges[0]:
    queue.append((next, 1))

while queue:
    current, depth = queue.popleft()
    if current == 0:
        print(depth)
        exit()
    if visited[current]:
        continue
    visited[current] = 1
    for next in edges[current]:
        queue.append((next, depth + 1))

print(-1)
