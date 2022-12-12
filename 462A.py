a = int(input())

st = ""

for i in range(a):
	x = input()
	st = st+x

print("YES" if st==st[::-1] else "NO" )