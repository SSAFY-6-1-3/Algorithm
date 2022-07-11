

def solution(n, build_frame):
    ans = [[0] * (n+1) for _ in range(n+1)]  # 0: 없음 1:기둥 2:보 3:둘다

    def is_bo(x, y):
        if x < n and ans[y-1][x+1] % 2: # 오른쪽 밑에 기둥
            return True
        if ans[y-1][x] % 2:    # 밑에 기둥
            return True
        if x in range(1, n) and ans[y][x-1] >= 2 and ans[y][x+1] >= 2:    # 양쪽이 보
            return True
        return False

    def is_gi(x, y):
        if not y:   # 바닥
            return True
        if ans[y-1][x] % 2:    # 밑에 기둥
            return True
        if x and ans[y][x-1] >= 2:  # 왼쪽에 보
            return True
        if x < n and ans[y][x+1] >= 2: # 오른쪽에 보
            return True
        return False

    def del_bo(x, y):
        if



    for bf in build_frame:
        x, y, a, b = bf

        if a and b: # 보 설치
            if is_bo(x, y):
                ans[y][x] = 2
        elif not a and b: # 기둥 설치
            if is_gi(x, y):
                ans[y][x] = 1
        elif a and not b: # 보 삭제
            pass
        elif not a and not b: # 기둥 삭제
            pass



    return ans

print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))

# def del_bo(x, y):
#     if x < n and ans[y][x+1]:
#         return False
#     if x and ans[y][x-1] == 2:
#         return False
#     return True
#
# def del_gi(x, y):
#     if y < n :
#         if ans[y+1][x] == 1:
#             return False
#         elif ans[y+1][x] == 2:
#             if x < n and ans[y][x+1] == 2:
#                 return True
#             return False
#         if x and ans[y+1][x-1]: return False