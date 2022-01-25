from collections import deque

def bfs(wires, start, wire, visited):
    que = deque([start])
    cnt = 1
    while que:
        q = que.popleft()
        for nums in wires:
            if q in nums and wire != nums:
                for num in nums:
                    if num != q and visited[num] == 0:
                        visited[num] = 1
                        cnt += 1
                        que.append(num)
    return cnt

def solution(n, wires):
    answer = n
    for wire in wires:                              # wires에서 하나씩 제외하기
        result = []
        visited = [0] * (n+1)
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = 1
                cnt = bfs(wires, i, wire, visited)
                result.append(cnt)

        answer = min(answer, abs(result[0]-result[1]))

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))