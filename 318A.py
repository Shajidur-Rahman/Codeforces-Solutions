a,b = list(map(int, input().split()))

li = []

li1 = []
li2 = []

for i in range(1,a):
	if i%2 != 0:
		li1.append(i)
	else:
		li2.append(i)

li = li1+li2


if len(li)<b:
	print(li[-1])
else:
	print(li[b-1])