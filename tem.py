t = int(input())

for i in range(t):


    a,b = list(input().split())



    a2 = list(set(a))
    b2 = list(set(b))


    a1 = "".join(a2)
    b1 = "".join(b2)

    if a1=="XS" and b=="M":
        print("<")
    elif a1 == "XS" and b=="XL":
        print("<")

    elif a1 == "XS" and b=="S":
        print("<")

    elif a1 == "M" and b=="L":
        print("<")

    elif a1 == "M" and b=="XL":
        print("<")

    elif a1 == "S" and b=="L":
        print("<")

    elif a1 == "S" and b=="XL":
        print("<")

    elif a1 == "S" and b=="M":
        print("<")

    elif a1 == "L" and b=="XL":
        print("<")

    elif a1==b1:

        if len(a)>len(b):
            if a1=="XS":
                print("<")
            else:

                print(">")
        elif len(a) == len(b):
            print("=")
        else:
            print("<")

    else:
        print(">")
