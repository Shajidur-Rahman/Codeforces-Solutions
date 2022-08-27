n,k=map(int,input().split()) #4,10
l=list(map(int,input().split())) # 4,3,1,2
c=0
p=max(l) # 4
a=[] 
while k>=0: 
	m=min(l) #1
	if m==p+1: #1==5
		break
	k-=m #k==k-m 10-1 
	c+=1 # 1
	if k<0:
		c-=1
		break
	else:
		i=l.index(m) #3 
		a.append(i+1) #4
		l[i]=p+1
print(c)
print(*a)
	