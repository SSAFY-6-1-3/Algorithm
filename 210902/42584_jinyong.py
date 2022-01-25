def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer[i] = j-i
                break
            else:
                answer[i] = len(prices)-i-1
    return answer


print(solution([1, 2, 3, 2, 3]))
