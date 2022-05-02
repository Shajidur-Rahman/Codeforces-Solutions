    
time = int(input())

yes = 0
final = 0

for time in range(0,time):
    a,b,c = (input()).split()

    a = int(a)
    b = int(b)
    c = int(c)

    

    if a==1:
        yes = yes + 1
    
    if b==1:
        yes = yes + 1
    
    if c==1:
        yes = yes + 1
    
    if yes >= 2:
        final = final + 1
    yes = 0
    
print(final)
    
