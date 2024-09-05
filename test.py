from collections import Counter

for i in range(31):
    for j in range(5):
        print((i >> j) & 1)

print(bin(31))
