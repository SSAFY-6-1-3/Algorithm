N = int(input())
wires = [list(map(int, input().split())) for _ in range(N)]
wires.sort(key=lambda x: x[0])

cnt = [0] * 500
for i in range(N):
    for j in range(i):
        if wires[j][1] < wires[i][1] and cnt[i] < cnt[j]:
            cnt[i] = cnt[j]
    cnt[i] += 1
max_cnt = max(cnt)
print(N - max_cnt)

'''
# 앞에서부터 전기줄 cnt하면 틀림...
N = int(input())
wires = [list(map(int, input().split())) for _ in range(N)]
wires.sort(key=lambda x: x[0])

max_cnt = 0
for i in range(N):
    tmp = 1
    now = wires[i][1]
    for j in range(i + 1, N):
        if now < wires[j][1]:
            now = wires[j][1]
            tmp += 1
    max_cnt = max(max_cnt, tmp)

print(N - max_cnt)
'''

