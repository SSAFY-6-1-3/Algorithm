# def sortsort(li):
#     # li.sort(key= lambda x: x[1])
#     # li.sort(key= lambda x: x[0])
#     li.sort(key= lambda x: (x[0], x[1]))
#     return li
#

import sys
input=sys.stdin.readline # 입력 속도 문제였다.
# i
N = int(input())
li = []
for _ in range(N):
    li.append(list(map(int, input().split())))
li.sort(key= lambda x: (x[0], x[1]))
# sortsort(li)

for i in range(N):
    print(*li[i]) # 시간초과
    # for k in range(2):
    #     print(li[i][k], end=' ')
    # print()