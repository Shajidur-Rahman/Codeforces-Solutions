for _ in range(int(input())):
    a,b=input().split(' ')
    s=0
    x=0
    c={}
    for i in a:
        if i=='S':
            s=(-2)len(a)
        if i=='L':
            s=len(a)
        if i=='M':
            s=(-1)len(a)
    for i in b:
        if i=='S':
            x=(-2)len(b)
        if i=='L':
            x=len(b)
        if i=='M':
            x=(-1)len(b)
    if s>x:
        print('>')
    if s<x:
        print('<')
    if s==x:
        print('=')
