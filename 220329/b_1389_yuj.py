from collections import deque

N, M = map(int, input().split())
friends = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    friends[A].append(B)
    friends[B].append(A)

person, num = N+1, (N+1)**2
for i in range(1, N+1):
    check = [0] * (N + 1)
    check[0] = 1                            # check할 때 안 걸리려고 본인은 1로 설정
    deq = deque([[i, 0]])
    while deq:
        now, cnt = deq.popleft()
        for friend in friends[now]:
            if not check[friend]:
                deq.append([friend, cnt + 1])
                check[friend] = cnt + 1

    if sum(check)-1 < num:
        person = i
        num = sum(check)-1

print(person)


