def solution(prices):
    answer = []
    L = len(prices) # 전체 길이 저장
    for price in range(L): # 각 초의 가격을 순회
        sec = L - price - 1 # 현재부터 마지막까지 값이 떨어지지 않았을 때의 시간
        for i in range(price+1, L): # 현재 뒤의 값 중에
            if prices[i] < prices[price]: # 더 낮은 값이 있으면
                sec = i-price # 그 시간을 저장하고 break
                break
        answer.append(sec) # sec값을 answer에 저장

    return answer

print(solution([1, 2, 3, 2, 3]))