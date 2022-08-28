a=int(input())#0
b=int(input())#1
for i in range(a):
  print(i+1, end=" ")
print(a+b+1, end=" ")#2
for j in range(b):
  print(a+b-j, end=" ")#1