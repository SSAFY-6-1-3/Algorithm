prices = [1, 2, 3, 2, 3]
answer = []

for i in range(len(prices)-1):              # 마지막일 경우 항상 0초이니까 비교할 필요 없음
    cnt = 0
    for j in range(i+1, len(prices)):       # 현재값(i) 뒤에 나오는 모든 값과 비교
        if prices[i] <= prices[j]:          # 현재값보다 크거나 같을 경우 가격이 유지되는 것이기 때문에 cnt +1
            cnt += 1
        else:
            cnt += 1                        # 그렇지 않을 경우 1초만 유지 -> 1 더해주고 break
            break
    answer.append(cnt)
answer.append(0)                        # 마지막값(0) 추가
print(answer)



# 다른 풀이
# popleft는 시간복잡도가 1 , pop(0)은 시간 복잡도가 list의 길이
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer