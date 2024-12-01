n, m = map(int, input().split())

ans = []


def search(depth, path, stretch):
    if depth == n:
        ans.append(tuple(path))
        return

    for i in range(stretch + 1):
        path.append(path[-1] + 10 + i)
        search(depth + 1, path, stretch - i)
        path.pop()


for first in range(1, m - (10 * n - 9) + 2):
    path = [first]
    search(1, path, m - (10 * n - 9) - (first - 1))

print(len(ans))
for i in ans:
    print(*i)
