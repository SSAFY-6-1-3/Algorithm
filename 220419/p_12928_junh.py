def solution(n):
    answer = n
    for i in range(1, n//2+1):
        if not n%i:
            answer += i
    return answer

print(solution(12))