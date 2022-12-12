a,b = list(map(int,input().split()))

c = sum(list(map(int, input().split())))

if c%b != 0:
	print((c//b)+1)
else:
	print(c//b)