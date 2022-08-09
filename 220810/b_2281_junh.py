import sys

input = sys.stdin.readline
n, m = map(int, input().split())
names = [int(input()) for _ in range(n)]
# [[마지막 칸, 마지막으로 쓴 글자 idx]]
lines = [[0, -1]]

for name in names:
    line = lines[-1]
    if line[0] + bool(line[0]) + name > m:
        lines.append([0, line[1]])
        line = lines[-1]
    line[0] += bool(line[0]) + name
    line[1] += 1
print(lines)

sum = 0
for i in range(len(lines)-1):
    a = (m - lines[i][0]) ** 2 + (m - lines[i+1][0]) ** 2
    last = lines[i][1]
    changed = True
    while changed:
        changed = False
        if lines[i+1][0] + 1 + names[last] <= m:
            b = (m - lines[i][0] + 1 + names[last]) ** 2 + (m - lines[i+1][0] - 1 - names[last]) ** 2
            if a > b:
                lines[i] = [lines[i][0] - 1 - names[last], lines[i][1] + 1]
                lines[i+1][0] = lines[i+1][0] + 1 + names[last]
                last = lines[i][1]
                a = b
                changed = True
    print(i, a)
    sum += (m - lines[i][0]) ** 2
print(lines)
print(sum)

'''
6 10
1
4
1
1
4
8
'''