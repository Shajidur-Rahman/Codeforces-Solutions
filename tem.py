time = int(input())

for i in range(time):


    a = int(input())


    x = input()
    y = input()

    x1 = 0
    y1 = 0

    if "R" in x:
        x1 = x1+1
    if "G" in x:
        x1 = x1+1
    if "B" in x:
        x1 = x1+1

    if "R" in y:
        y1 = y1+1
    if "G" in y:
        y1 = y1+1
    if "B" in y:
        y1 = y1+1

        

    if (x.count("B") == a and x.count("G")):
        print("YES")
    elif (x.count("R") == a and x.count("G") == a) or (x.count("R") == a and x.count("B") == a):
        print("NO")
    elif x1==y1:
        print("YES")
    else:
        print("NO")