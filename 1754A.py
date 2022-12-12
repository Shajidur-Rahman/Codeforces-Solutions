t = int(input())

for i in range(t):
	a = int(input())
	x = input()
	if (x.count("Q") > x.count("A")) or x[-1] == "Q" or x[0] == "A":
		print("No")
	else:
		print("Yes")