n = int(input())
n1 = n//2

a = input()

x = a.count("x")
X = a.count("X")

_max = max(x,X)

required = abs(_max-n1)

print(required)
if required != 0:
	if "XX" in a:
		a = a.replace("XX","Xx",required)
	if "xx" in a:
		a = a.replace("xx", "Xx",required)

print(a)