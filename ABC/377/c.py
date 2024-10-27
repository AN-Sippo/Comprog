n, m = map(int, input().split())

dangers = set()
for _ in range(m):
    ai, bi = map(int, input().split())
    dangers.add((ai, bi))
    for i, j in [
        (ai + 2, bi + 1),
        (ai + 1, bi + 2),
        (ai - 1, bi + 2),
        (ai - 2, bi + 1),
        (ai - 2, bi - 1),
        (ai - 1, bi - 2),
        (ai + 1, bi - 2),
        (ai + 2, bi - 1),
    ]:
        if 1 <= i <= n and 1 <= j <= n:
            dangers.add((i, j))

print(n**2 - len(dangers))
