n = int(input())

point_lst = []

for _ in range(n):
    point_lst.append(list(map(int, input().split())))

answer = sorted(point_lst, key=lambda x: (x[0], x[1]))

for ans in answer:
    print(*ans)
