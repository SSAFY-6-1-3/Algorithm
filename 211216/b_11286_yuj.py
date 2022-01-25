import sys
sys.stdin=open('input.txt')
# 최소 힙
import heapq

q = []
N = int(input())
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        heapq.heappush(q, (abs(num), num))      # 절댓값을 우선순위로 가지게 된다
        print(q)
    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)

