n, m = map(int, input().split())
alst = list(map(int, input().split()))
blst = list(map(int, input().split()))

blst = [(v, i) for i, v in enumerate(blst)]
blst.sort(reverse=True)
ans = [-1 for _ in range(m)]
a_idx = 0
for value, idx in blst:
    while a_idx < n and value < alst[a_idx]:
        a_idx += 1
    if a_idx == n:
        ans[idx] = -1
        continue
    ans[idx] = a_idx + 1

for i in ans:
    print(i)
