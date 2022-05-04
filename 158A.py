# codeforces.com's problems' solution
# problem no 158A
# count, target = input().split()

# a = input().split()
# print(a)

# final = 0

# for i in range(0,int(count)):
#     if a[i-1] > target:
#         final = final+1


# print(final)


# count, target = input().split()

# a = input().split()

# for i in range(0,int(count)):
#     if target in a:
#         a.remove(target)
#     elif int(a[i]) < 2:
#         a.remove(a[i])

# print(len(a))


def main():
	from sys import stdin, stdout

	inp = [int(x) for x in stdin.read().split()]

	n = inp.pop(0)
	k = inp.pop(0)

	k_th = inp[k-1]
	cnt = 0

	for x in inp:
		if x and x >= k_th:
			cnt += 1;

	stdout.write(str(cnt) + '\n')

main()