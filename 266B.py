a,b = list(map(int, input().split()))
x = input()

while b:
	x = x.replace("BG", "GB")
	b = b -1 

print(x)