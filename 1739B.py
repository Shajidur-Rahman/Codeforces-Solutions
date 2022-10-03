t = int(input())

for i in range(t):


	a = int(input())

	x = list(map(int,input().split()))

	y = []
	y.append(x[0])

	def task(x):
		for i in range(1,len(x)):
			y.append(y[-1] + x[i])

		for i in range(len(y)):
			print(y[i], end=" ")
		print()


	if x[-1]<x[-2]:
		print(-1)
	else:
		task(x)


