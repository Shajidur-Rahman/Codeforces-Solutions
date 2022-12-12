n = int(input())
a = list(map(int, input().split()))

a.sort()

my_coins = []
my_coins.append(a[-1])
a.pop()

while sum(a) >= sum(my_coins):
	my_coins.append(a[-1])
	a.pop()

print(len(my_coins))
