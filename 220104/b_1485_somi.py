# 틀림

def length(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2


tc = int(input())

for _ in range(tc):
    points = [list(map(int, input().split())) for _ in range(4)]

    points.sort(key=lambda x: (x[0], x[1]))
    s1 = length(points[0], points[2])
    s2 = length(points[1], points[3])
    if s1 != s2:
        print(0)
        break

    s3 = length(points[0], points[1])
    s4 = length(points[2], points[3])

    if s3 != s4 or s2 != s3:
        print(0)
        break

    d1 = length(points[3], points[0])
    d2 = length(points[1], points[2])

    if d1 != d2 or 2 * s1 != d1:
        print(0)

    else:
        print(1)