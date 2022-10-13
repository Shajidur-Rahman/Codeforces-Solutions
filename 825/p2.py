import math

t = int(input())

for v in range(t):

    c = input()
    a = list(map(int, input().split()))
    for i in range(len(a) - 1):

        if math.gcd(a[i], a[i + 2]) > math.gcd(a[i], a[i + 1]):
            print("No")
        else:
            print("Yes")
