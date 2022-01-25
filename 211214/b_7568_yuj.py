N = int(input())
people = []
result = [0] * N
for idx in range(N):
    x, y = map(int, input().split())
    people.append((x, y, idx))

people.sort()
result[people[-1][2]] = 1
print(people)
for i in range(N-1):
    cnt = 1
    for j in range(i+1, N):
        if people[i][1] < people[j][1] and people[i][0] < people[j][0]:
            cnt += 1
    result[people[i][2]] = cnt
print(*result)