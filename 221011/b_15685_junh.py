
N = int(input())
starts = []
for _ in range(N):
    starts.append(list(map(int, input().split())))

dY = (0, -1, 0, 1)
dX = (1, 0, -1, 0)


print(starts)


def build(y, x, d, g, stack):

    while stack:
