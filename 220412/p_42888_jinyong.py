def solution(record):
    answer = []

    user_dic = {}
    record_list = []

    for i in record:
        i = i.split(" ")
        if i[0] != 'Change':
            record_list.append(i[:2])
        if i[0] == 'Leave':
            continue
        user_dic[i[1]] = i[2]

    for i in record_list:
        if i[0] == 'Enter':
            answer.append(user_dic[i[1]] + '님이 들어왔습니다.')
        else:
            answer.append(user_dic[i[1]] + '님이 나갔습니다.')

    return answer
