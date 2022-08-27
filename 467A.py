rooms = int(input())

rooms_emty = 0

for i in range(rooms):
	a,b = list(map(int, input().split()))
	if (b-a) >= 2:
		rooms_emty = rooms_emty + 1
	else:
		pass

print(rooms_emty)