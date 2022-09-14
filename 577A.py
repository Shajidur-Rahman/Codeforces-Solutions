a,b = list(map(int, input().split()))

total = 0

for i in range(1,a+1):
	if b%i==0 and b/i<= a:
		total = total + 1
	else:
		pass




print(total)