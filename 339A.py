# codeforces.com's problems' solution
# problem no 339A
a = input().split("+")
a.sort()
for i in range(len(a)):
    if i == len(a)-1:
        print(a[i])
    else:
        print(a[i] + "+", end="")