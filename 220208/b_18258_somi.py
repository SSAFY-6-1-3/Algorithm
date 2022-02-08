import sys

N = int(input())
q = []
idx = 0  # front index

for _ in range(N):
    word = sys.stdin.readline().strip()

    if word == "pop":
        if len(q) - idx > 0:
            print(q[idx])
            idx += 1
        else:
            print(-1)

    elif word == "size":
        print(len(q) - idx)
    elif word == "empty":
        if len(q) - idx > 0:
            print(0)
        else:
            print(1)
    elif word == "front":
        if len(q) - idx > 0:
            print(q[idx])
        else:
            print(-1)
    elif word == "back":
        if len(q) - idx > 0:
            print(q[-1])
        else:
            print(-1)
    else:
        q.append(word[5:])