n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

vertex = [[] for _ in range(n+1)]
for i, j in edge:                  # 인접 리스트
    vertex[i].append(j)
    vertex[j].append(i)

dist = [0] * (n+1)                 # 1로부터의 거리
dist[1] = 1
queue = [1]                        # 연결된 노드
idx = 0

for _ in range(n):
    num = queue[idx]               # idx 늘려가면서 다음 노드 확인
    cnt = dist[num]                # dist에 저장된 크기 + 1 (1로부터의 거리)
    for n in vertex[num]:
        if not dist[n]:            # 방문한 적 없는 노드이면 queue에 추가, 거리 저장
            dist[n] = cnt+1
            queue.append(n)
    idx += 1

result = 0
for i in dist:                     # 최대값 개수 세기
    if i == max(dist):
        result += 1

print(result)