def solution(n, computers):
    answer = 0
    for i in range(n):
        q = [i]
        flag = False
        while q:
            now = q.pop()
            for j in range(n):
                if computers[now][j]:
                    q.append(j)
                    computers[now][j] = 0
                    computers[j][now] = 0
                    flag = True
        if flag:
            answer += 1
    return answer

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])