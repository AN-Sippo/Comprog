from collections import deque

n = int(input())
hlst = list(map(int, input().split()))

ans = [0 for _ in range(n)]


l = deque()
for i in reversed(range(n)):
    hi = hlst[i]
    ans[i] = len(l)
    while l and l[0] < hi:
        l.popleft()
    l.appendleft(hi)

print(*ans)
