a,b = list(map(int, input().split()))

x = list(map(int, input().split()))

total = 0

for i in range(a):
	if x[i] > b:
		total = total + 2
	else:
		total = total + 1 

print(total)