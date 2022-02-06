import sys
from collections import deque

input = sys.stdin.readline

def comm(st, q):
    if len(st) >= 6:
        _, n = st.split()
        q.append(int(n))

    elif st == "size":
        print(len(q))

    elif st == "empty":
        if q:
            print(0)
        else:
            print(1)

    elif not q:
        print(-1)

    elif len(st) == 3:
        print(q.popleft())

    elif st == "front":
        print(q[0])

    else:
        print(q[-1])


N = int(input())
q = deque()
for _ in range(N):
    comm(input().rstrip(), q)