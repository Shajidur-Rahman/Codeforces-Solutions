n = int(input())
a = list(map(int, input().split()))

li = []

for i in range(n-1):
	d = a[i+1] -a[i]
	li.append(d)

d2 = a[2]-a[0]
li.append(d2)

if max(li) > d2:
	print(max(li))
else:
	print(d2)