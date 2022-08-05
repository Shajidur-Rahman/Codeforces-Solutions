a = [[],[],[],[],[]]

a[0] = list(map(int, input().split()))
a[1] = list(map(int, input().split()))
a[2] = list(map(int, input().split()))
a[3] = list(map(int, input().split()))
a[4] = list(map(int, input().split()))

row = 0
column = 0
total = 0
ope = []

for i in range(5):
    if 1 in a[i]:
        ope = a[i]
        row = i + 1


        if row > 3:
            total = total + row-3
        elif row < 3:
            total = 3-row + total        


        ope = list(ope)
        sear = 1
        sear = ope.index(1) + 1


        if sear > 3:
            total = total + sear -3
        elif sear < 3:
            total = total + 3-sear



print(total)