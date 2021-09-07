"""
주식가격 떨어지지 않은 기간은 몇 초인지 return
"""

# sol2. pop안쓰고 for문 돌리니 통과!
def solution(prices):
    answer = [0] * len(prices)  # 답 출력할 리스트
    for i in range(len(prices)):  # 가격 순서대로 순환
        for j in range(i + 1, len(prices)):  # 다음 가격들과 비교
            answer[i] += 1  # 가격이 떨어지면 1초간 떨어지지 않은 것으로 보기 때문에 일단 증가
            if prices[i] > prices[j]:  # 만약 다음 가격 떨어지는 경우 더이상 비교 필요 없음
                break
    return answer


# sol1. 시간초과....
def solution(prices):
    answer = [0] * len(prices)  # 답 출력할 리스트 생성
    i = 0  # answer 인덱스
    while len(prices):  # 가격이 남아있는 경우
        price = prices.pop(0)  # 첫번 째 가격 pop
        for j in range(len(prices)):  # 남아있는 가격들과 비교했을 때,
            if price <= prices[j]:    # 가격이 떨어지지 않았다면 1 증가
                answer[i] += 1
            else:                     # 가격이 떨어지면 1초간 떨어지지 않은 것으로 봄
                answer[i] += 1
                break
        i += 1 # answer 인덱스 증가
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))