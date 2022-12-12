x = int(input())
for i in range(x):
        
    a,b,c,d = list(map(int, input().split()))

    v1 = a/b
    v2 = c/d

    if v1 == v2:
        print(0)

    elif v1 == 0 or v2 == 0:
        print(1)

    elif b/d == int(b/d) or d/b == int(d/b):
        print(1)

    elif v1 != int(v1) or v2 != int(v2):
        print(2)
    else:
        print(1)