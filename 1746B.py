# t = int(input())

# for i in range(t):
#     b = int(input())
#     x = input()

#     zero = x.count("0")

#     ans = 0

#     for i in range(b):
#         if x[i] == 0:
#             zero -= 1 
#         else:
#             if zero > 0:
#                 ans +=1
#             else:
#                 zero -= 1




t = int(input())

for i in range(t):
    b = int(input())
    x = input()

    zero = x.count("0")

    ans = 0

    for i in range(b):
        if x[i] == 0:
            zero -= 1 
        else:
            if zero > 0:
                ans +=1
                zero -= 1