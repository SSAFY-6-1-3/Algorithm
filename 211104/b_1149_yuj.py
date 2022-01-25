import sys
sys.stdin=open('input.txt')

# DP
# 색상이 세가지니까 그 전에 사용할 수 있는 색상은 두 개밖에 없음
# 그 두 개 중에 더 작은 걸로 갱신
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    R, G, B = arr[i-1][0], arr[i-1][1], arr[i-1][2]
    arr[i][0] += min(G, B)
    arr[i][1] += min(R, B)
    arr[i][2] += min(R, G)

print(min(arr[-1]))