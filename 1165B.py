a = int(input())

b = sorted(list(map(int, input().split())))

k = 1

for i in range(len(b)):
	if b[i] >= k:
		k+=1

print(k-1)