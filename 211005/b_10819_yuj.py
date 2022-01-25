import sys
from itertools import permutations  # 순열 사용
sys.stdin=open('input.txt')

def cal(j):
    global maxv
    answer = 0
    for i in range(N-1):
        answer += abs(result[j][i] - result[j][i+1])
    if maxv < answer:
        maxv = answer


N = int(input())
lst = list(map(int,input().split()))
result = list(permutations(lst, N))         # 순열 이용해서 숫자 순서 모두 구하기
maxv = 0
for j in range(len(result)):                # 모든 순열의 차이 구하기 -> 그 중 최댓값 출력
    cal(j)
print(maxv)