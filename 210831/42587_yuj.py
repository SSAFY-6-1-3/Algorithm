

def solution(priorities, location):
    answer = 0
    idx_lst = list(enumerate(priorities))
    result = []
    while idx_lst:
        for _ in range(len(idx_lst)-1):
            if idx_lst[0][1] < idx_lst[1][1]:
                idx_lst.append(idx_lst.pop(0))
            else:
                idx_lst.append(idx_lst.pop(1))

        result.append(idx_lst.pop(0))

    for i in range(len(result)):
        if result[i][0] == location:
            answer += i+1
            break
    return answer


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))