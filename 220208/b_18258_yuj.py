import sys
input = sys.stdin.readline
from collections import deque

deq = deque([])
N = int(input().rstrip())
for _ in range(N):
    command = input().rstrip()
    if 'push' in command:
        com, num = map(str, command.split())
        deq.append(num)
    elif 'size' == command:
        print(len(deq))
    else:
        if deq:
            if 'pop' == command:
                print(deq.popleft())
            elif 'back' == command:
                print(deq[-1])
            elif 'front' == command:
                print(deq[0])
            else:
                print(0)
        else:
            if 'empty' == command:
                print(1)
            else:
                print(-1)