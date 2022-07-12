

def solution(n, build_frame):
    mat = [[0] * (n+1) for _ in range(n+1)]  # 0: 없음 1:기둥 2:보 3:둘다

    def is_bo(x, y):
        if x < n and mat[y-1][x+1] % 2: # 오른쪽 밑에 기둥
            return True
        if mat[y-1][x] % 2:    # 밑에 기둥
            return True
        if x in range(1, n) and mat[y][x-1] >= 2 and mat[y][x+1] >= 2:    # 양쪽이 보
            return True
        return False

    def is_gi(x, y):
        if not y:   # 바닥
            return True
        if mat[y-1][x] % 2:    # 밑에 기둥
            return True
        if x and mat[y][x-1] >= 2:  # 왼쪽에 보
            return True
        if mat[y][x] >= 2: # 오른쪽에 보
            return True
        return False

    def del_bo(x, y):
        mat[y][x] -= 2

        if mat[y][x] and not is_gi(x, y):   # 현재 위치 기둥 검사
            mat[y][x] += 2
            return

        if x < n :  # 오른쪽
            if mat[y][x+1] >= 2 and not is_bo(x+1, y):  #보
                mat[y][x] += 2
                return

            if mat[y][x+1] % 2 and not is_gi(x+1, y):   #기둥
                mat[y][x] += 2
                return

        if x and mat[y][x-1] >= 2 and not is_bo(x-1, y): # 왼쪽 보
            mat[y][x] += 2
            return


    def del_gi(x, y):
        mat[y][x] -= 1

        if y < n:
            if mat[y+1][x] % 2 and not is_gi(x, y+1):   # 기둥
                mat[y][x] += 1
                return
            if mat[y+1][x] >= 2 and not is_bo(x, y+1):  # 보
                mat[y][x] += 1
                return

            if x and mat[y+1][x-1] >= 2 and not is_bo(x-1, y+1):    # 왼쪽 보
                mat[y][x] += 1
                return




    for bf in build_frame:
        x, y, a, b = bf

        if a and b: # 보 설치
            if is_bo(x, y):
                mat[y][x] += 2
        elif not a and b: # 기둥 설치
            if is_gi(x, y):
                mat[y][x] += 1
        elif a and not b: # 보 삭제
            del_bo(x, y)
        elif not a and not b: # 기둥 삭제
            del_gi(x, y)


    ans = []
    for i in range(n+1):
        for j in range(n+1):
            if mat[j][i] % 2:
                ans.append([i, j, 0])
            if mat[j][i] >= 2:
                ans.append([i, j, 1])

    return ans

print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
