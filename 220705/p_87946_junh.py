def solution(k, dungeons):
    answer = -1

    def dfs(eng, visited):
        nonlocal answer
        answer = max(answer, len(visited))

        for i in range(len(dungeons)):
            if i not in visited:
                need, cost = dungeons[i]
                if need <= eng :
                    dfs(eng-cost, visited.union({i}))

    dfs(k, set())

    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))

print(solution(80, [[80, 20], [50, 40], [30, 10]]))