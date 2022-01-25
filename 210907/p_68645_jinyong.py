def solution(n):
    answer = []
    result = []
    move = [(1, 0), (0, 1), (-1, -1)]
    move_idx = 0

    maximum = 0
    for i in range(1, n+1):
        answer.append([0] * i)
        maximum += i

    cur_r, cur_c = -1, 0
    number = 1
    while number <= maximum:
        new_r = cur_r + move[move_idx][0]
        new_c = cur_c + move[move_idx][1]

        if not(0 <= new_r < n and 0 <= new_c < len(answer[new_r])):
            move_idx = (move_idx + 1) % 3
            continue

        if answer[new_r][new_c] == 0:
            answer[new_r][new_c] = number
            number += 1
            cur_r = new_r
            cur_c = new_c

        else:
            move_idx = (move_idx + 1) % 3

    for ans in answer:
        result.extend(ans)

    return result


print(solution(6))