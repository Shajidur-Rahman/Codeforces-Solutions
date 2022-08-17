levels = int(input())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

yes = 0

li = []

for i in range(0,levels+1):
    li.append(i)

numbers = a[0]
a.remove(a[0])

x = set((a+b))

x = list(x)

x.sort()

for i in range(len(li)):
    if li[i] in x:
        yes = 0
    else:
        yes = 1
    
if yes == 1:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")