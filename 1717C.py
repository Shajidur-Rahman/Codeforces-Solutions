n = int(input())

# li1 = list(map(int, input().split()))
# li2 = list(map(int, input().split()))


li1 = [1,2,3,4,5]
li2 = [6,5,6,7,6]

# def solve(li1, li2):
# 	for i in range(n):
# 		if li1[i] == li2[i]:
# 			continue
# 		else:
# 			if i<n


# while li1 != li2:
# 	solve(li1, li2)




# if ai+1  if i<n and ai≤ai+1, or i=n and  ai≤a1

a = 0

for i in range(li2[a]):
	if li1[a] == li2[a]:
		print("Yes")
		continue
	else:
		if (a < n and li1[a] <= li1[a+1] ) or i == n and li1[a] <= li1[1]:
			print("No")
			li1[a] +=1

