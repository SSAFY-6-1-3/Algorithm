def rotate(mat, M):                             # 90도 회전
    new_mat = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new_mat[j][M-1-i] = mat[i][j]
    return new_mat

def check(mat, M, N):                           # 자물쇠 0과 키 1이 더해져서 자물쇠 모든 부분이 1인지 확인
    for x in range(M-1, M+N-1):                 # 0이면 자물쇠에 키가 안 맞음, 1이상이면 자물쇠 돌기와 열쇠 돌기가 만남
        for y in range(M-1, M+N-1):
            if mat[x][y] != 1:
                return False
    return True

def solution(key, lock):
    M = len(key)
    N = len(lock)
    new_lock = [[0] * (2*M+N-2) for _ in range(2*M+N-2)]    # 중간에 자물쇠를 기준으로 matrix 확장
    cnt = 0
    for i in range(N):
        for j in range(N):
            if lock[i][j]:
                new_lock[M-1+i][M-1+j] = 1
                cnt += 1

    key2 = rotate(key, M)
    key3 = rotate(key2, M)
    key4 = rotate(key3, M)
    keys = [key, key2, key3, key4]

    for key in keys:
        for i in range(M+N-1):                              # 자물쇠 시작을 한 칸씩 이동시키면서 자물쇠랑 키를 겹쳐봄
            for j in range(M+N-1):
                for x in range(M):
                    for y in range(M):
                        new_lock[i+x][j+y] += key[x][y]

                if check(new_lock, M, N):                   # 자물쇠가 풀리는지 확인
                    return True

                for x in range(M):                          # 원래 자물쇠로 되돌리기
                    for y in range(M):
                        new_lock[i+x][j+y] -= key[x][y]

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))