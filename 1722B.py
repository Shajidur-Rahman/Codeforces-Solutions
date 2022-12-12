time = int(input())

for i in range(time):
	a = int(input())

	x1 = input()
	x2 = input()

	x1 = x1.replace("B", "G")
	x2 = x2.replace("B", "G")
	if x1 == x2:
		print("YES")
	else:
		print("NO")