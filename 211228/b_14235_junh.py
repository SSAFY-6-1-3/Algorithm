import heapq
import sys

input = sys.stdin.readline  # 이거 넣으면 틀림...


N = int(input())
gifts = []
heapq.heapify(gifts)

for _ in range(N):
    a = input()
    if a == '0\n':
        # print(123)        # a == '0'이 안되는 듯. a가 0\n으로 들어오고 있음
        if gifts:
            print(-heapq.heappop(gifts))
        else:
            print(-1)
    else:
        list_a = list(map(int, a.split()))
        for i in range(1, len(list_a)):
            heapq.heappush(gifts, -list_a[i])
