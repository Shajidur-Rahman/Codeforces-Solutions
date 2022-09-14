time = int(input())

for i in range(time):
		

	a = int(input())

	b = list(map(int, input().split()))

	bMin = min(b)

	total = 0

	for i in range(a):
		if b[i] != bMin:
			total = total + (b[i] - bMin )

	print(total)