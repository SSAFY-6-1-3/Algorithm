import sys

input = sys.stdin.readline

def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5



N = int(input().rstrip())
for _ in range(N):
    points = [list(map(int, input().rstrip().split())) for _ in range(4)]
    points.sort()
    a, b, c, d = points

    if dist(a, b) == dist(a, c) == dist(d, b) == dist(d, c) and dist(a, d) == dist(b, c):
        print(1)
    else:
        print(0)

