import heapq

N = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)

for _ in range(N-1):
    li = list(map(int, input().split()))

    for n in li:
        heapq.heappush(heap, n)
        heapq.heappop(heap)

print(heap[0])




# mat = [list(map(int, input().split())) for _ in range(N)]
# # start = max(mat[N-1])
#
# st_hubo = sorted(enumerate(mat[N-1]), key=lambda x:-x[1])
# rank = [st_hubo[i][0] for i in range(N)]
# answer = []
#
# # q = deque([(N-1, rank[0])])
# hubos = [(N-1, 0)]
#
# while len(answer) < N:
#     hubos.sort(key= lambda x:mat[x[0]][rank[x[1]]])
#
#     mx_y, mx_x = hubos.pop()
#     mx_rx = rank[mx_x]
#     answer.append(mat[mx_y][mx_rx])
#
#     if mx_y: hubos.append((mx_y - 1, mx_x))
#     if mx_x < N: hubos.append((mx_y, mx_x + 1))
#
# print(answer[N-1])







