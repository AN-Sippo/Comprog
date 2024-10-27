n, m = map(int, input().split())
segments = []
for _ in range(n):
    li, ri = map(int, input().split())
    segments.append((ri, li))
segments.sort(reverse=True)
l = 1
ans = 0
for r in range(1, m + 1):
    while segments and segments[-1][0] == r:
        ri, li = segments.pop()
        l = max(li + 1, l)
    else:
        diff = r - l + 1
        ans += r - l + 1
print(ans)
