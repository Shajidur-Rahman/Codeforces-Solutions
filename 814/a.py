a = int(input())

for i in range(a):
    x,y = list(map(int, input().split()))

    if (x == 1 and y == 1) or (x%2 == 0 and y%2 == 0):
        print("Tonya")
    else:
        print("Burenka")