n = int(input())
a = list(map(int, input().split()))

final = max(a)

while final > 0:

	for i in range(n+1,2,-1):
		a[n-1] += a[n-1]-a[n-2]

	print(final)	