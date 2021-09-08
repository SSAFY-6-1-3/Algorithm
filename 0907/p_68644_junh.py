def solution(numbers):
    len_n = len(numbers)
    n_set = set() # 중복을 막기위해 set
    for i in range(len_n - 1): # 제일 뒤의 숫자는 할 필요 x
        for k in range(i+1, len_n):
            n_set.add(numbers[i] + numbers[k]) # 합을 set에 넣는다.
    answer = list(n_set) # 리스트로 변환
    return sorted(answer) # 정렬하여 return



print(solution([2,1,3,4,1]))