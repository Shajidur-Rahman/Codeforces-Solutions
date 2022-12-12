a = input()

li = ['A','H','I','M','O','T','U','V','W','X','Y']

yes = 0

for i in range(len(a)):
	if a[i] in li:
		pass
	else:
		yes = 1
		break

if yes == 0 and a == a[::-1]:
	print("YES")
else:
	print("NO")