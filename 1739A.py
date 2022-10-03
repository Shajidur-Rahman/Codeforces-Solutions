t = int(input())

for i in range(t):


	a,b = list(map(int , input().split()))

	if a == 1 or b == 1:
		print(a,b)
	elif a == 3 and b == 3:
		print(2,2)
	elif a == 2 and b == 3:
		print(2,2)
	elif a == 3 and b==2:
		print(2,2)
	else:
		print(a,b)