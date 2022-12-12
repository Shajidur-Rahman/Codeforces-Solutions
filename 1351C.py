# a = input()

# second = 5

# du = ["N", "S"]
# du2 = ["W","E"]

# for i in range(1,len(a)):
# 	if a[i] == a[i-1]:
# 		second += 5
# 	elif a[i] == du[0] and a[i-1] == du[1]:
# 		second += 1
# 	elif a[i] == du[1] and a[i-1] == du[0]:
# 		second += 1
# 	elif a[i] == du2[0] and a[i-1] == du2[1]:
# 		second += 1
# 	elif a[i] == du2[1] and a[i-1] == du2[0]:
# 		second += 1
# 	else:
# 		second += 5

# print(second)



a = input()

second = 0

e = a.count("E")
w = a.count("W")
n = a.count("N")
s = a.count("S")

if e != 0 and w != 0:
	second = second + e*5+w
	e = 0
	w = 0
if n != 0 and s != 0:
	second = second + n*5+s 
	n = 0
	s = 0 
second = second + n*5
second = second + e*5
second = second + s*5
second = second + w*5

print(second)