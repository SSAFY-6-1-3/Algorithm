N = int(input())
cage = list([0, 0, 0] for _ in range(N + 1))

cage[1][0], cage[1][1], cage[1][2] = 1, 1, 1
# 배치 안함, 왼쪽에 배치, 오른쪽에 배치

for i in range(2, N + 1):
    cage[i][0] = (cage[i - 1][0] + cage[i - 1][1] + cage[i - 1][2]) % 9901
    cage[i][1] = (cage[i - 1][0] + cage[i - 1][2]) % 9901
    cage[i][2] = (cage[i - 1][0] + cage[i - 1][1]) % 9901

print(sum(cage[N]) % 9901)
