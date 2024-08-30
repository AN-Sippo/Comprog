def permutations(l: list[int]):
    N = len(l)
    l.sort()
    ans = [l]
    solve(ans, l)
    for i in ans:
        print(i)
    print(f"total:{len(ans)}")


def solve(ans, l: list[int]):
    N = len(l)
    i = N - 2
    while l[i] > l[i + 1]:
        i -= 1
    if i < 0:
        return
    j = N - 1
    while l[j] < l[i]:
        j -= 1
    nl = swap(l, i, j)
    nl = nl[: i + 1] + nl[:i:-1]
    ans.append(nl)
    solve(ans, nl)


def swap(l, a, b):
    ll = [i for i in l]
    ll[a], ll[b] = ll[b], ll[a]
    return ll


permutations([1, 2, 3, 4, 5])
