def solution(name):
    up_down = 0
    to_go = [0]

    for i in range(len(name)):
        chr = name[i]
        a = ord('A')
        b = ord(chr)

        tmp = abs(b - a)
        if tmp:
            to_go.append(i)

        if 26 - tmp < tmp:
            tmp = 26 - tmp
        up_down += tmp

    min_move = len(name) ** 2

    def permu(visited, move):
        nonlocal min_move
        if move > min_move:
            return
        if len(visited) == len(to_go):
            min_move = move

        now_idx = visited[-1]

        for next_idx in range(len(to_go)):
            if next_idx in visited:
                continue
            visited.append(next_idx)
            dist = abs(to_go[next_idx] - to_go[now_idx])
            if dist > len(name) // 2 :
                dist = len(name) - dist
            permu(visited, move + dist)
            visited.pop()

    permu([0], 0)
    return up_down + min_move



print(solution("JEROEN"))
print(solution("JAN"))