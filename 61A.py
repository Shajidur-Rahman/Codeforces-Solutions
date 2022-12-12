a = input()
b = input()

st = []

for i in range(len(a)):
	if a[i] == b[i]:
		st.append("0")
	else:
		st.append("1")

print("".join(st))