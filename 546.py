a,b,c = list(map(int, input().split()))

casts = 0

for i in range(0,c+1):
    casts = casts + a*i
print(casts - b)