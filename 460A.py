a,b = list(map(int, input().split()))

if int(a/b) == 1:
	print(int((a/b)+a))
else:
	print(int((a/b)+a + 1))