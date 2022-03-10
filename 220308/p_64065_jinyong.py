def solution(s):
    answer = []
    tuple_s = s[2:-2].split('},{')
    list_s = []

    for word in tuple_s:
        list_s.append(list(map(int, word.split(','))))
    list_s_sort = sorted(list_s, key=lambda x: len(x), reverse=False)

    answer.append(list_s_sort[0][0])

    for i in range(1, len(list_s_sort)):
        answer.append(list(set(list_s_sort[i]) - set(list_s_sort[i - 1]))[0])

    return answer
