def solution(array, commands):
    answer = []
    for command in commands:
        s, e, t = command
        cut = array[s-1:e]
        cut.sort()
        answer.append(cut[t-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))