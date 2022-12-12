
t = int(input())

for i in range(t):

	a,b,c = list(map(int, input().split()))

	f1=0
	f2=0

	f1 = a-1
	if b>c:
		f2 = (b-c) + c-1
	else:
		f2 = (c-b) + c - 1


	if f1<f2:
		print(1)
	elif f2<f1:
		print(2)
	else:
		print(3)