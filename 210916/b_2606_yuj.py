import sys
sys.stdin = open('input.txt')

num = int(input())
N = int(input())
arr = [[0] * (num+1) for _ in range(num+1)]

for _ in range(N):
    i, j = map(int, input().split())
    arr[i][j] = arr[j][i] = 1                       # 연결된 컴퓨터들 (i,j)(j,i)에 1로 표시

worm = [1]                                          # 1번 컴퓨터
checked = [1]                                       # 바이러스 걸린 컴퓨터를 중복해서 찾지 않기 위해 list 사용

while worm:                                         # 1번 컴퓨터로부터 연결된 컴퓨터 모두 찾기
    i = worm.pop()

    for j in range(1, num + 1):
        if arr[i][j] == 1 and (j not in checked):      # 바이러스에 걸렸는데 검사하지 않은 컴퓨터라면
            worm.append(j)                             #
            checked.append(j)

print(len(checked)-1)                       # 1번 컴퓨터 제외





