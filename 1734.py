t = int(input())

for i in range(t):

	x = int(input())
	a = list(map(int, input().split()))

	a.sort()

	c = max(a)

	c1 = 0
	c2 = 2

	for i in range(x-2):
		c = min((a[c2]-a[c1]), c)
		c1+=1
		c2+=1

	print(c)