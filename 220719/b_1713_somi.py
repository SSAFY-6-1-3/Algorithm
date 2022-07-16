N = int(input())  # 사진틀 개수
total = int(input())  # 전체 학생 총 추천 수
recom = list(map(int, input().split()))  # 추천받은 학생 번호
board = dict()  # 홈페이지 {학생 번호 : [추천수, 날짜]}

for i in range(total):
    num = recom[i]  # 학생 번호
    if num in board:
        board[num][0] += 1
        board[num][1] = i
        continue

    if len(board) == N:  # 꽉차면, 추천 횟수 가장 적은 학생 삭제
        min_cnt = 1000
        student = 0
        for s, tmp in board.items():
            if tmp[0] < min_cnt:
                min_cnt = tmp[0]
                student = s
        del board[student]

    board[num] = [1, i]
print(*sorted(board.keys()))

'''
heqpq로 풀이 틀림

import heapq

for i in range(total):

    for pic in board:
        if pic[2] == recom[i]:
            pic[0] += 1
            pic[1] = i
            break
    else:
        if len(board) == N:
            heapq.heappop(board)
        heapq.heappush(board, [1, i, recom[i]])

ans = list(str(num[2]) for num in board)
ans.sort()
print(' '.join(ans))
'''