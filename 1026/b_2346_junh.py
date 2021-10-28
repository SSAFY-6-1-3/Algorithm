from collections import deque
q = deque([])
def boom(n, balloons):
    rtn = []
    idx = 0

    for _ in range(n-1):
        rtn.append(idx+1)
        move = abs(balloons[idx])
        one = 1
        if balloons[idx] < 0:
            one = -1

        balloons[idx] = 0
        cnt = 0
        while cnt<move:
            idx = (n+ idx + one)%n
            if balloons[idx]:
                cnt +=1

    for i in range(n):
        if balloons[i]:
            rtn.append(i+1)
            break
    return rtn


N = int(input())
balloons = list(map(int, input().split()))
print(*boom(N, balloons))
