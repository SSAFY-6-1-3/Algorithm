import sys
from collections import deque

input = sys.stdin.readline
def solut(A, B):
    q = deque([(A, "")])
    visited = [False] * 10000
    visited[A] = True

    while q:
        n, step = q.popleft()

        d = (2*n) % 10000
        s = (n+9999) % 10000
        l = (n%1000)*10 + n//1000
        r = (n%10) * 1000 + n//10
        com = {"D": d, "S": s, "L":l, "R":r}

        for k, v in com.items():
            if v == B:
                return step+k
            if visited[v]: continue
            visited[v] = True
            q.append((v, step+k))



T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(solut(A, B))
