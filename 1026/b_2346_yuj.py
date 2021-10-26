import sys
sys.stdin=open('input.txt')
from collections import deque
'''
이동해야할만큼 pop 하고, 뒤로 다시 append 시킴 
-> 다음에 터져야 할 풍선을 맨 앞으로 보내고, 다음 순서에 popleft 시켜서 터뜨림
'''
N = int(input())
papers = [0] + list(map(int, input().split()))      # 풍선 번호랑 인덱스 맞춰주기
ballons = deque([i for i in range(1, N+1)])
result = []

while True:
    ballon = ballons.popleft()
    result.append(ballon)

    if not ballons:                                 # 다 터뜨렸다면 break
        break

    paper = papers[ballon]                          # 이동해야하는 크기 확인

    if paper < 0:                                   # 이동해야하는 크기가 음수라면(왼쪽으로 이동해야한다면)
        while paper < 0:                            # 남아있는 풍선의 길이만큼 더해줘서 양수로 만들어줌
            paper += len(ballons)
        paper += 1

    for _ in range(paper - 1):                      # 이미 시작 풍선을 터뜨렸기 때문에
        temp = ballons.popleft()                    # 다음에 터져야할 풍선이 맨 앞에 오려면 paper-1번 터져야 함
        ballons.append(temp)

print(*result)