from sys import setrecursionlimit

setrecursionlimit(10**6)


def solve():
    n, k = map(int, input().split())
    plst = list(map(lambda x: int(x) - 1, input().split()))
    dic_l = {}
    dic_idx = {}
    visited = [0 for _ in range(n)]

    def search(i, l):
        if visited[i]:
            return
        visited[i] = 1
        l.append(i)
        dic_l[i] = l
        dic_idx[i] = len(l) - 1
        search(plst[i], l)

    for i in plst:
        if visited[i]:
            continue
        l = []
        search(i, l)

    # for i, v in dic_l.items():
    #     print(f"{i}:{v} at {dic_idx[i]}")
    #     print("")

    ans = [0 for _ in range(n)]
    for i, pi in enumerate(plst):
        length = len(dic_l[pi])
        assert pi == dic_l[pi][dic_idx[pi]]

        idx = (dic_idx[pi] + pow(2, k, length) - 1) % length
        ans[i] = dic_l[pi][idx] + 1

    print(*ans)


solve()
