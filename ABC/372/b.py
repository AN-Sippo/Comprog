m = int(input())

ans = []

for i in range(20):
    for j in reversed(range(11)):
        v = 3**j
        if v <= m:
            m -= v
            ans.append(j)
            break

    if m == 0:
        break
print(len(ans))
print(*ans)
