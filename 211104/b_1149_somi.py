N = int(input())
homes = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    homes[i][0] = min(homes[i-1][1], homes[i-1][2]) + homes[i][0]
    homes[i][1] = min(homes[i - 1][0], homes[i - 1][2]) + homes[i][1]
    homes[i][2] = min(homes[i - 1][0], homes[i - 1][1]) + homes[i][2]

print(min(homes[-1]))

# paint = [homes[0]] + list([0] * 3 for _ in range(N - 1))
# for home in range(1, N):
#     paint[home][0] = min(paint[home-1][1], paint[home-1][2]) + homes[home][0]
#     paint[home][1] = min(paint[home - 1][0], paint[home - 1][2]) + homes[home][1]
#     paint[home][2] = min(paint[home - 1][0], paint[home - 1][1]) + homes[home][2]
#
# print(min(paint[-1]))