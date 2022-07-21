from collections import deque

N, M = map(int, input().split())
board = [0] * 101
visited = [0] * 101
for _ in range(N+M):
    x, y = map(int, input().split())
    board[x] = y

visited[1] = 1
deq = deque([[1, 0]])
while deq:
    [num, cnt] = deq.popleft()
    for i in range(1, 7):
        if num+i in range(101) and not visited[num+i]:
            visited[num+i] = cnt+1
            if board[num+i]:
                if not visited[board[num+i]]:
                    visited[board[num+i]] = cnt+1
                deq.append([board[num+i], cnt+1])
            else:
                deq.append([num + i, cnt + 1])

print(visited[-1])