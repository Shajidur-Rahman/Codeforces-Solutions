a,b = list(map(int, input().split()))
x = list(map(int, input().split()))

_max = max(x)

c = len(x) - x[::-1].index(max(x)) - 1

if _max > b:
	print(c)
else:
	print(x.index(x[-1])+1)