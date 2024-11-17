n = input()
one = 0
two = 0
three = 0
for ni in n:
    if ni == "1":
        one += 1
    elif ni == "2":
        two += 1
    elif ni == "3":
        three += 1
print("Yes" if (one == 1 and two == 2 and three == 3) else "No")
