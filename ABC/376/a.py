n, c = map(int, input().split())
tlst = list(map(int, input().split()))
ans = 0
prev = 0
for i in range(n):
    if i == 0:
        ans += 1
        prev = tlst[i]
        continue
    if tlst[i] - prev >= c:
        prev = tlst[i]
        ans += 1

print(ans)
