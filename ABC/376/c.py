n = int(input())
alst = list(map(int, input().split()))
blst = list(map(int, input().split()))

alst.sort(reverse=True)
blst.sort()

buy = 0
for i in range(n):
    ai = alst[i]
    if not blst:
        print(ai)
        exit()
    bi = blst[-1]
    if bi >= ai:
        blst.pop()
        continue
    else:
        if buy != 0:
            print(-1)
            exit()
        buy = ai
print(buy)
