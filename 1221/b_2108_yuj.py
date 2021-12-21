import sys
from collections import Counter
input=sys.stdin.readline
# counter 모듈 사용 -> 딕셔너리 형태로 바꿔줌
# most_common -> 데이터의 개수가 많은 순으로 정렬 (튜플 형태로 정렬)
def find(nums):
    counter = Counter(nums).most_common()
    if counter[0][1] == counter[1][1]:
        return counter[1][0]
    else:
        return counter[0][0]

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()
print(round(sum(nums)/N))
print(nums[N//2])
if N > 1:
    print(find(nums))
else:
    print(nums[0])
print(abs(nums[-1]-nums[0]))