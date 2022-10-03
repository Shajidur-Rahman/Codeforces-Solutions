n = int(input())
a = list(map(int, input().split()))

x = len(a) - a[::-1].index(min(a)) - 1
y = a.index(max(a))

print(x,y)