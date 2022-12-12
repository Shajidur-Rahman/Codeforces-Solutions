# codeforces.com's problems' solution
# problem no 110A
a = input()

number = a.count("4") + a.count("7")

if number == 4 or number == 7:
    print("YES")
else:
    print("NO")