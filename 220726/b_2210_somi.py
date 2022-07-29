directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(r, c):
    stack = [(r, c, arr[r][c])]
    while stack:
        now_r, now_c, num = stack.pop(-1)
        if len(num) == 6:
            if num not in numbers:
                numbers.add(num)
            continue

        for i in range(4):
            next_r, next_c = now_r + directions[i][0], now_c + directions[i][1]
            if 0 <= next_r < 5 and 0 <= next_c < 5:
                next_num = num + arr[next_r][next_c]
                stack.append((next_r, next_c, next_num))


arr = list(input().split() for _ in range(5))
numbers = set()

for x in range(5):
    for y in range(5):
        dfs(x, y)

print(len(numbers))

