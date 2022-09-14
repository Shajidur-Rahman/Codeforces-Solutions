# time = int(input())

# for i in range(time):
# 	x,y = list(map(int, input().split()))

# 	if y%x != 0:
# 		print(0,0)
# 	else:
# 		print(1,int(y/x))




t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if y % x != 0:
        print(0, 0)
    else:
        print(1, y // x)