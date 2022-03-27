def solution(record):

    translate = {'Enter': '님이 들어왔습니다.',
                 'Leave': '님이 나갔습니다.'}
    nicks = {}
    chats = []
    for r in record:
        now = r.split()
        do, id = now[0], now[1]

        if do == 'Enter' or do == 'Change':
            nicks[id] = now[2]

        if do == 'Enter' or do == 'Leave':
            chats.append((id, do))

    answer = []
    for chat in chats:
        answer.append(nicks[chat[0]] + translate[chat[1]])

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))