can_put = [[1 for _ in range(8)] for _ in range(8)]

for i in range(8):
    si = input()
    for j in range(8):
        if si[j] == "#":
            for ii in range(8):
                can_put[i][ii] = 0
            for jj in range(8):
                can_put[jj][j] = 0

print(sum([sum(i) for i in can_put]))
