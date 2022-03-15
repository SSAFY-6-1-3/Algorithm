N = int(input())

visited = [False for _ in range(N + 1)]
q = [(N, 0)]
while q:
    num, time = q.pop(0)
    if num == 1:
        print(time)
        break

    next_num = [num - 1]
    if num % 3 == 0:
        next_num.append(num//3)
    if num % 2 == 0:
        next_num.append(num//2)

    for n in next_num:
        if not visited[n]:
            q.append((n, time + 1))
            visited[n] = True
