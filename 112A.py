# codeforces.com's problems' solution
# problem no 112A
a = input()
b = input()

a = a.lower()
b = b.lower()

if a==b:
    print(0)
elif a>b:
    print(1)
elif a<b:
    print(-1)

    