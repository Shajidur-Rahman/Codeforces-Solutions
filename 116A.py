# codeforces.com's problems' solution
# problem no 116A
c = int(input())

li = []

statu = 0

while c>0:
    
    a,b = input().split()
    a = int(a)
    b = int(b)

    statu = (statu-a)+b
    li.append(statu)

    c = c-1

print(max(li))