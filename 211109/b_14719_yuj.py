import sys
sys.stdin=open('input.txt')

height, width = map(int, input().split())
blocks = list(map(int, input().split()))
arr = [[0] * height for _ in range(width)]          # 블럭을 90도 돌리기

for w in range(width):
    block = blocks[w]
    for idx in range(block):
        arr[w][idx] = 1

result = 0
for j in range(height):
    cnt = 0
    check = []
    for i in range(width):
        if arr[i][j] == 1:
            check.append(i)

    if len(check) > 1:
        for k in range(len(check)-1, 0, -1):
            cnt += (check[k] - check[k-1] - 1)
        result += cnt

print(result)
