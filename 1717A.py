# import math

# time = int(input())

# for i in range(time):

# 	a = int(input())

# 	times = 0

# 	for i in range(1,a+1):
# 		for i2 in range(1,a+1):		
# 			lcm = math.lcm(i,i2)
# 			gcd = math.gcd(i,i2)


# 			if lcm/gcd <= 3:
# 				times = times+1
# 			else:
# 				pass


# 	print(times)




for i in range(int(input())):
    x=int(input())
    print(x+2*(x//2)+2*(x//3))