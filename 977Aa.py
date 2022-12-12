# codeforces.com's problems' solution
# problem no 977A
a,b = input().split()
a = int(a)
b = int(b)

for i in range(b):
    if a%10 == 0:
        a = a/10
    else:
        a = a -1
    
print(int(a))