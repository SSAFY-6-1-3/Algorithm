import sys
from collections import deque
N = int(sys.stdin.readline())

card_q = deque()
for i in range(1, N+1):
    card_q.append(i)

while len(card_q) > 1:              # 카드가 하나 남을 때까지 반복
    card_q.popleft()                # 제일 위의 카드 버리고
    first = card_q.popleft()        # 그 다음 위의 카드 
    card_q.append(first)            # 밑으로 이동


print(card_q[0])