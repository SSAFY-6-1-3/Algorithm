'''
좌표정렬하기
sort, sorted 의 key 인자로 비교할 함수를 넣어주면 함수의 반환값을 비교해서 정렬
lambda 인자 : 리턴값
비교할 아이템 요소가 복수이면, 튜플로 그 순서를 알려주면 됨.
'''
import sys
sys.stdin = open('input.txt')


N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
xy.sort(key = lambda x: (x[0], x[1]))

'''
시간초과
for i in range(N):
    x, y = xy[i]
    print(int(x), int(y))
'''
for i in range(N):
    print(xy[i][0], xy[i][1])