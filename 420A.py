a = input()

if a == a[::-1] and len(a)>1:
	print("YES")
else:
	print("NO")