t = int(input())

for i in range(t):
	n = int(input())
	a = list(map(int,input().split()))

	if n==1:
		print(1)
	elif len(set(a)) == 1:
		print(0)
	else:
		print(max(a))