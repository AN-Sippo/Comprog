l, r = map(int, input().split())
if l == 1 and r == 0:
    print("Yes")
elif r == 1 and l == 0:
    print("No")
else:
    print("Invalid")
