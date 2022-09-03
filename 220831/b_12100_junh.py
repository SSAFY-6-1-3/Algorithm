import sys

input = sys.stdin.readline
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = max(max(matrix[i]) for i in range(N))


def garo(mat, d, depth):
    global answer

    new_mat = []
    for i in range(N):
        stack = []
        if d == "l":
            line = mat[i]
        elif d == "r":
            line = mat[i][::-1]
        elif d == "u":
            line = [mat[j][i] for j in range(N)]
        elif d == "d":
            line = [mat[j][i] for j in range(N-1, -1, -1)]

        j = 0
        tmp = 0
        while j < N:
            n = line[j]
            if n == 0:
                pass
            elif tmp == n:
                stack.append(n*2)
                tmp = 0
            else:
                if tmp:
                    stack.append(tmp)
                tmp = n
            j += 1
        stack.append(tmp)
        new_mat.append(stack + [0] * (N - len(stack)))

    if depth == 4:
        answer = max(answer,  max(max(new_mat[i]) for i in range(N)))
    elif mat != new_mat:
        for d in "lrud":
            garo(new_mat, d, depth+1)


for d in "lrud":
    garo(matrix, d, 0)
print(answer)