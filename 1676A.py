time = int(input())

for i in range(time):


	a = input()

	n1 = 0
	n2 = 0

	for i in range(6):
		if i <=2:
			n1 = int(a[i]) + n1
		else:
			n2 = int(a[i]) + n2

	if n1 == n2:
		print("YES")
	else:
		print("NO")