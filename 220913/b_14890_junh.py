
N, L = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]


def check(line):
    def build(start, drc):
        nonlocal std
        plus = (drc == -1)
        for i in range(plus, L + plus):
            idx = start + i * drc
            if idx not in range(N) or used[idx] or line[idx] != std - (not plus):
                return False

        for i in range(plus, L + plus):
            used[start + i * drc] = True
        std -= drc
        return True

    used = [False] * N
    std = line[0]
    idx = 0
    while idx < N:
        if not used[idx]:
            if line[idx] == std:
                pass
            elif line[idx] == std + 1:
                if not build(idx, -1):
                    return False
            elif line[idx] == std - 1:
                if not build(idx, 1):
                    return False
            else:
                return False
        idx += 1
    return True


cnt = 0
for l in mat:
    if check(l):
        cnt += 1
mat = list(zip(*mat))
for l in mat:
    if check(l):
        cnt += 1
print(cnt)



# import sys; R = sys.stdin.readline
# n, l = map(int,R().split())
# board = [[*map(int,R().split())] for _ in range(n)]
#
# def able(row):
#     cont = 1; up = True
#     for i in range(1,n):
#         gap = row[i]-row[i-1]
#         if abs(gap)>1: return False
#         if gap==-1:
#             if not up and cont<l: return False
#             cont = 1; up = False
#         elif gap==1:
#             if not up and cont<2*l: return False
#             if cont<l: return False
#             cont = 1; up = True
#         else: cont += 1
#     if not up and cont<l: return False
#     return True
#
# print(sum(able(row) for row in board)+sum(able([board[i][j] for i in range(n)]) for j in range(n)))