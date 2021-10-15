import sys

input = sys.stdin.readline

def hello(idx, hp, hpn):
    global max_gain

    if hp <= 0:
        return
    if hpn > max_gain:
        max_gain = hpn

    for i in range(idx+1, N):
        if not helloed[i]:
            helloed[i] = True
            hello(i, hp - cost[i], hpn+gain[i])
            helloed[i] = False





N = int(input())
cost = list(map(int, input().split()))
gain = list(map(int, input().split()))
helloed = [False] * N
max_gain = 0
hello(-1, 100, 0)
print(max_gain)