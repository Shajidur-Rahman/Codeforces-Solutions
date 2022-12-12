# t = int(input())

# li = []

# for i in range(t):
# 	a = (input())
# 	li.append(a)



# if t == 1:
# 	print(1)
# 	exit()

# elif li.count("10") == 1 and li.count("10") == 1:
# 	print(2)
# elif li.count("10")%2 == 0 and li.count("01")%2 == 0:
# 	print(2)
# else:
# 	print(3)


a = int(input())

li = []
group = 1

for i in range(a):
	c = int(input())
	li.append(c)

for i in range(a-1):
	if li[i] != li[i+1]:
		group+=1
	else:
		pass

print(group)