# time = int(input())

# for i in range(time):


# 	a,b = list(map(int, input().split()))

# 	c = list(map(int, input().split()))

# 	li1 = set(c)
# 	li2 = list(li1)

# 	cost = len(li1) * b

# 	for i in range(len(li2)):
# 		if c.count(li2[i]) < 2:
# 			cost = cost - 1

# 	if len(c)==1:
# 		print(1)
# 		exit()

# 	print(cost)

# time = int(input())

# for i in range(time):

# 	a,b = list(map(int, input().split()))
# 	c = list(map(int, input().split()))

# 	li = set(c)
# 	li2 = list(li)

# 	d1 = 0
# 	d2 = 0

# 	for i in range(len(li2)):
# 		if c.count(li2[i]) == 1:
# 			d1+=1

# 		else:
# 			d2+=b

# 	print(min((d1+d2), len(c)))


time = int(input())

for i in range(time):

	a,b = list(map(int, input().split()))
	c = list(map(int, input().split()))

	li1 = set(c)
	li2 = list(li1)

	s = 0
	d = 0

	for i in range(len(li2)):
		if li2.count(li2[i]) == 1:
			s+=1
		else:
			d+=1

	print(min((s+d*b),a))

