time = int(input())

for i in range(time):	

		x= input()
		y= input()

		a,b,c,d = x[0],x[1],y[0],y[1]

		li = [a,b,c,d]

		li2 = set(li)

		z = (len(list(li2)))

		print(z-1)