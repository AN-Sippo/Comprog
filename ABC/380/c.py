from itertools import groupby


n, k = map(int, input().split())
s = input()
lst = groupby(s)
ans = []
cnt = 0
tmp = ""
for key, value in lst:
    if key == "1":
        cnt += 1
    if cnt == k - 1 and key == "0":
        tmp = len(list(value))
    else:
        ans.append(key * len(list(value)))

    if cnt == k and key == "1":
        ans.append("0" * tmp)


for i in ans:
    print(i, end="")
print()
