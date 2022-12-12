import re

a = input()

if re.search("hello", a):
	print("YES")
else:
	print("NO")