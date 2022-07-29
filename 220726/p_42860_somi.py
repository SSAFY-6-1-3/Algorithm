def solution(name):
    now_word = 'A' * len(name)
    up_down = sum(list(min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) for char in name))

    q = [(now_word, 0, 0)]  # (현재 문자, 커서 위치, 지금까지 왼 / 오 이동 횟수)
    side = len(name) * 27  # 왼 / 오 최소 이동 횟수 저장

    if up_down == 0:  # 문자가 모두 'A'로 이루어진 경우
        return 0

    while q:
        word, index, cnt = q.pop(0)
        next_word = word[:index] + name[index] + word[index+1:]

        if cnt > side:  # 가지치기
            continue

        if next_word == name:
            side = min(side, cnt)

        for i in [-1, 1]:  # 왼, 오 이동
            next_index = (index + len(word) + i) % len(word)
            next_cnt = cnt + 1
            q.append((next_word, next_index, next_cnt))

    return side + up_down

