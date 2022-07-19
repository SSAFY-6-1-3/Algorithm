def solution(word):
    answer = 0
    moem = 'AEIOU'
    stop = False

    def dfs(idx, st):
        nonlocal answer, stop
        for i in range(idx, 5):
            tmp = st + moem[i]
            answer += 1

            if tmp == word:
                stop = True
                return
            if len(tmp) == 5:
                continue
            dfs(idx, tmp)
            if stop:
                return

    dfs(0, "")

    return answer


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))