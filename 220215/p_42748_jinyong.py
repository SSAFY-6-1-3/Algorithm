def solution(array, commands):
    answer = []
    for lst in commands:
        print(lst)
        temp_list = []
        for i in range(lst[0], lst[1]+1):
            temp_list.append(array[i-1])
            temp_list.sort()
        answer.append(temp_list[lst[2]-1])
    return answer