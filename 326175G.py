a,b,c = list(map(float, input().split()))

d = (a*b)/c

if d != int(d):
	print("double")
elif d > 2147483647 or d< (-2147483648):
	print("long long")
else:
	print("int")