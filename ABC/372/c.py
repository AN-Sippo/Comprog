n, q = map(int, input().split())
s = list(input())


def get(i):
    if i >= n:
        return ""
    elif i < 0:
        return ""
    else:
        return s[i]


count = 0

for i in range(n):
    if s[i] == "A":
        if get(i + 1) == "B" and get(i + 2) == "C":
            count += 1

for _ in range(q):
    xi, ci = input().split()
    xi = int(xi) - 1
    if (
        (get(xi - 1) == "B" and get(xi - 2) == "A" and get(xi) == "C")
        or (get(xi - 1) == "A" and get(xi) == "B" and get(xi + 1) == "C")
        or (get(xi) == "A" and get(xi + 1) == "B" and get(xi + 2) == "C")
    ):
        count -= 1
    if ci == "A":
        if get(xi + 1) == "B" and get(xi + 2) == "C":
            count += 1
    elif ci == "B":
        if get(xi - 1) == "A" and get(xi + 1) == "C":
            count += 1
    elif ci == "C":
        if get(xi - 1) == "B" and get(xi - 2) == "A":
            count += 1

    s[xi] = ci
    print(count)
