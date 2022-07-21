# 큰 사각형에서 포함 안 되는 작은 사각형 빼기
K = int(input())
dic = {1: [], 2: [], 3: [], 4: []}
prev_d, prev_l = 0, 0
dirs = [[1, 3], [4, 1], [2, 4], [3, 2]]      # 작은 사각형이 나오는 경우가 정해져있음
square = 0
first = 0
for j in range(6):
    d, l = map(int, input().split())
    if j == 0:
        first = l
    dic[d].append(l)
    for i in range(4):
        if dirs[i][1] == d and dirs[i][0] == prev_d:
            square = l * prev_l
    prev_d = d
    prev_l = l

if square == 0:                         # 패인 사각형 모서리에서 시작하는 경우
    square = prev_l * first             # 가장 처음 변 * 가장 마지막 변 = 작은 사각형

width = max(dic[1], dic[2])[0]
length = max(dic[3], dic[4])[0]
print((width*length-square)*K)