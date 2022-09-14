# def solve(x,y,z):
# 	answer = 0

# 	for i in x:
# 		if i in y and i in z:
# 			continue
# 		elif i in y or i in z:
# 			answer += 1
# 		else:
# 			answer += 3

# 	return answer

# time = int(input())

# for a in range(time):

# 	d = int(input())

# 	x = input().split()
# 	y = input().split()
# 	z = input().split()
# 	answer = (solve(x,y,z), solve(y,x,z), solve(z,x,y))
# 	print(*answer)





T = int(input())
def solve(u,v,w):
	ans = 0
	for word in u:
		if word in v and word in w:
			continue
		elif word in v or word in w:
			ans += 1
		else:
			ans += 3
	return ans
for _ in range(T):
	n = int(input())
	u = set(input().split())
	v = set(input().split())
	w = set(input().split())
	ans = [solve(u,v,w),solve(v,u,w),solve(w,u,v)]
	print(*ans)