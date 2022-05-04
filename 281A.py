# codeforces.com's problems' solution
# problem no 281A
a = input()

if a[0] == a[0].capitalize():
    print(a)
else:
    x = a[0].capitalize()
    y = a[1:]
    z = x+y
    print(z)