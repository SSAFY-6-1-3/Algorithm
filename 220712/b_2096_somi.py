N = int(input())
min_nums = [0] * 3
max_nums = [0] * 3

tmp_max = [0] * 3
tmp_min = [0] * 3

for _ in range(N):
    tmp = list(map(int, input().split()))
    # max
    tmp_max[0] = tmp[0] + max(max_nums[0], max_nums[1])
    tmp_max[1] = tmp[1] + max(max_nums)
    tmp_max[2] = tmp[2] + max(max_nums[1], max_nums[2])
    max_nums = tmp_max[:]
    # min
    tmp_min[0] = tmp[0] + min(min_nums[0], min_nums[1])
    tmp_min[1] = tmp[1] + min(min_nums)
    tmp_min[2] = tmp[2] + min(min_nums[1], min_nums[2])
    min_nums = tmp_min[:]

print(max(max_nums), min(min_nums))
'''
# 메모리 초과
def sum_num(r, c, num):
    global min_ans, max_ans
    if r == N - 1:
        max_ans = max(max_ans, num)
        min_ans = min(min_ans, num)
        return

    for i in range(-1, 2):
        if 0 <= i + c < N:
            sum_num(r + 1, i + c, num + numbers[r + 1][i + c])


N = int(input())
numbers = list(list(map(int, input().split())) for _ in range(N))
max_ans = 0
min_ans = float('inf')
for c in range(3):
    sum_num(0, c, numbers[0][c])

print(max_ans, min_ans)
'''



