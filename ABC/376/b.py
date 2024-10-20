def process(current, destination, obstacles):
    res = -1
    if current < obstacles and obstacles < destination:
        res = current + n - destination
    elif current > obstacles and obstacles > destination:
        res = destination + n - current
    else:
        res = abs(destination - current)

    return res


n, q = map(int, input().split())

l = 0
r = 1
ans = 0
for i in range(q):
    hi, ti = input().split()
    ti = int(ti) - 1
    if hi == "L":
        ans += process(l, ti, r)
        l = ti
    elif hi == "R":
        ans += process(r, ti, l)
        r = ti
print(ans)
