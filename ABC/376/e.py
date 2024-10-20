from heapq import heappush, heappop, heapify


def process():
    n, k = map(int, input().split())
    alst = list(map(int, input().split()))
    blst = list(map(int, input().split()))
    sorted_pairs = sorted(zip(alst, blst))

    # ソートされたペアからalstとblstをそれぞれ抽出
    alst = [pair[0] for pair in sorted_pairs]
    blst = [pair[1] for pair in sorted_pairs]
    # a_tree = SegmentTree(n, alst, 0, max)
    b_members = []
    b_sum = 0
    for bi in blst[:k]:
        heappush(b_members, -bi)
        b_sum += bi
    a_max = alst[k - 1]
    ans = a_max * b_sum
    for idx in range(k, n):
        max_a = alst[idx]
        bi = blst[idx]
        b_sum += heappop(b_members)
        b_sum += bi
        heappush(b_members, -bi)
        ans = min(ans, max_a * b_sum)
        # bi =

    print(ans)


t = int(input())
for _ in range(t):
    process()
