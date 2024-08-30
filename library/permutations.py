def permutations(l: list[int]):
    # l != []
    if len(l) == 1:
        return [l]
    res = []
    for i in range(len(l)):
        for li in permutations(l[:i] + l[i + 1 :]):
            res.append([l[i]] + li)

    return res
