def solution(name):
    answer = 0


    def dfs(now, dir, move):
        if now <= -len(name) or now >= len(name): return 0
        a = ord('A')
        b = ord(name[now])

        tmp = abs(b - a)
        if 26 - tmp < tmp:
            tmp = 26 - tmp

        # move += dfs(now+dir, dir, move+1)
        return move + tmp + dfs(now+dir, dir, 1)

    print(dfs(0, 1, 0))
    print(dfs(0, -1, 0))

    return answer



print(solution("JEROEN"))
print(solution("JAN"))