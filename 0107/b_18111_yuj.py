import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
ground = []
for _ in range(N):
    ground += list(map(int, input().split()))

max_height = max(ground)
min_height = min(ground)
result = [float('inf'), 0]

for h in range(min_height, max_height+1):
    inventory = B
    time = 0
    for i in range(N*M):
        if h < ground[i]:
            inventory += ground[i] - h
            time += 2 * (ground[i] - h)
        elif h > ground[i]:
            inventory -= h - ground[i]
            time += h - ground[i]

    if inventory >= 0:                      # 높이가 점점 높아지므로 전에 저장된 시간과 같은 시간일 경우
        if result[0] >= time:               # 높이는 더 높을 수밖에 없음
            result[0] = time
            result[1] = h

print(*result)