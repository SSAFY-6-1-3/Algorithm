import sys
sys.stdin=open('input.txt')

arr = [[0] * 101 for _ in range(101)]
cnt = 0
for _ in range(4):
    lx, ly, rx, ry = map(int, input().split())
    for x in range(lx, rx):
        for y in range(ly, ry):
            if not arr[x][y]:
                arr[x][y] = 1
                cnt += 1

print(cnt)