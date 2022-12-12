# codeforces.com's problems' solution
# problem no 791A
num_array = input().split()
 
num1 = int(num_array[0])
num2 = int(num_array[1])
count = 0
 
while num1 <= num2:
    num1 *= 3
    num2 *= 2
    count += 1
    
print(count)