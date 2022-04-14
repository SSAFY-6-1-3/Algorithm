def solution(record):
    answer = []
    users = {}
    for r in record:                                        # 바뀐 이름 미리 저장
        if 'Enter' in r or 'Change' in r:
            word, id, name = r.split()
            users[id] = name
    for re in record:
        if 'Change' not in re:
            if 'Enter' in re:
                word, id, name = re.split()
                res = f'{users[id]}님이 들어왔습니다.'
            elif 'Leave' in re:
                word, id = re.split()
                res = f'{users[id]}님이 나갔습니다.'
            answer.append(res)

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))