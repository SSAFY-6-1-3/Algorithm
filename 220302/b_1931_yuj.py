# 시작 시간으로도 정렬 필요
# (9,10)를 먼저 선택하면, (10,10)의 회의를 선택할 기회가 주어진다.
# 하지만, (10, 10)의 회의가 먼저 선택되면, 종료시간이 10을 넘어갔기 때문에 9시작은 고려되지 않는다.
N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort(key=lambda x: (x[1], x[0]))              # x[0] 따로 설정 안 해주면 정렬 안 됌
cnt, end = 0, -1
for time in times:
    if end <= time[0]:
        end = time[1]
        cnt += 1
print(cnt)