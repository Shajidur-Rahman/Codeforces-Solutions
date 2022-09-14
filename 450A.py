a,b = list(map(int, input().split()))
x = list(map(int, input().split()))

li = []

for i in range(a):
	if x[i] > b:
		li.append(x[i])

if len(li) == 0:
	print(a-sorted(x,reverse=True).index(x[0]))
else:
	print(a-sorted(x,reverse=True).index(li[-1]))