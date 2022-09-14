a = int(input())

x = list(map(int, input().split()))

a1 = x.count(1)
a0 = x.count(0)

count = 0

if a1==a:
    print(a)
elif a0 == a:
    print(0)
else:
    for i in range(1,len(x)):
        if x[i]-(x[i]-1) == 1:
            count += 1
        else:
            pass
    print(count)