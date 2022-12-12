# codeforces.com's problems' solution
# problem no 266A
def colored_stones(num, colors):
    count = 0
    for i in range(0, len(colors) - 1):
        if colors[i] == colors[i+1]:
            count += 1
        else:
            continue
    return count


if __name__ == '__main__':
    num = int(input())
    colors = input()
    print(colored_stones(num, colors))