time = int(input())
for i in range(time):
	a,b = sorted(list(map(int, input().split())))
	c,d = sorted(list(map(int, input().split())))
	print("YES" if b==d and a+c == d else "No")
