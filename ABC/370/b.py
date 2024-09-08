n = int(input())
alst = []
for _ in range(n):
    alst.append(list(map(int, input().split())))


def get(i, j):
    if i >= j:
        return alst[i - 1][j - 1]
    else:
        return alst[j - 1][i - 1]


before = 1
for i in range(1, n + 1):
    before = get(before, i)

print(before)
