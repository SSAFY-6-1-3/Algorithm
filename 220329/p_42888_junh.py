def solution(record):
    answer = []
    id_name = {}

    for rec in record:
        message = rec.split()
        mes, idd = message[0], message[1]
        if len(message)==3:
            name = message[2]
            id_name[idd] = name

    for rec in record:
        message = rec.split()
        mes, idd = message[0], message[1]
        if len(message) == 3:
            name = message[2]

        if mes == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(id_name[idd]))
        elif mes == 'Leave':
            answer.append("{}님이 나갔습니다.".format(id_name[idd]))


    return answer



print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))