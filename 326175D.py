a,b,c,d = list(map(int, input().split()))

li = []

li.append(a+b-c)
li.append(a-b+c)
li.append(a*b+c)
li.append(a+b*c)
li.append(a*b-c)
li.append(a-b*c)



if d in li:
	print("YES")
else:
	print("NO")