'''
n-qeens
아직 다 못품!!!
'''


def n_queens(i, col):
    count = 0
    n = len(col) - 1
    if promising(i, col):
        if i == n:
            count +=1
        else:
            for j in range(1, n + 1):
                col[j + 1] = j
                n_queens(i + 1, col)

def promising(i, col):
    k = 1
    flag = True
    while (k < i and flag):
        if (col[i] == col[k]) or abs(col[i] - col[k]) == abs(i-k):
            flag = False
            k +=1
    return flag

def solution(n):
    global answer


n_queens(1,)


