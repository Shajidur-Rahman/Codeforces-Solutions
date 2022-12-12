a,b = list(map(int, input().split()))

c = a*b

if c%2 == 0:
    print(int(c/2))
else:
    c = c-1
    print(int(c/2))