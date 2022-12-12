# codeforces.com's problems' solution
# problem no 71A

time = int(input())

for i in range(0,time):
    a = input()

    if len(a) > 10:


        print(a[0], end="")
        print(len(a) -2, end="")
        print(a[-1])
    else:
        print(a)