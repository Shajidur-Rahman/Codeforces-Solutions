# codeforces.com's problems' solution
# problem no 282A
time = int(input())

final = 0

for i in range(0,time):
    inp = input()
    if "X++" == inp or "++X" == inp:
        final = final + 1
    elif "--X" == inp or "X--" == inp:
        final = final -1
    else:
        pass

print(final)