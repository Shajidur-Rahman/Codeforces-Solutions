a, b, s = map(int, input().split())
s -= abs(a) + abs(b)
print('no' if s < 0 or s & 1 else 'yes')