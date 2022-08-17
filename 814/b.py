aaa = int(input())
for i in range(aaa):
    a,b = list(map(int, input().split()))

    li = [x for x in range(1,a+1)]
    li2 = list(reversed(li))
    pairs = []
    paris2  = pairs

    for i in range(len(li)):
        if len(li) != 0:
            s = li[0]
            ss = li[1]
            if ((li[0] + b)*li[1])%4 == 0:
                pairs.append(li[0])
                pairs.append(li[1])
            li.remove(s)
            li.remove(ss)


    for i in range(len(li2)):
        if len(li2) != 0:
            s = li2[0]
            ss = li2[1]
            if ((li2[0] + b)*li2[1])%4 == 0:
                paris2.append(li2[0])
                paris2.append(li2[1])
            li2.remove(s)
            li2.remove(ss)
    
    if len(pairs) != 0:
        print("YES")
        for i in range(len(pairs)):
            if len(pairs) != 0:
                z = pairs[0]
                zz = pairs[1]
                print(z,zz)
                pairs.remove(z)
                pairs.remove(zz)

        paris3 = list(reversed(paris2))

        for i in range(len(paris3)):
            if len(paris3) != 0:
                z = paris3[0]
                zz = paris3[1]
                print(z,zz)
                paris3.remove(z)
                paris3.remove(zz)

    else:
        print("NO")