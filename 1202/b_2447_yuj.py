import sys
sys.stdin=open('input.txt')

def star(n):

    if n == 1:
        return

    for m in range(N//n):
        for i in range((n//3)+n*m, (2*n//3)+n*m):
            for k in range(N // n):
                for j in range((n//3)+n*k, (2*n//3)+n*k):
                    pattern[i][j] = ''
    star(n//3)


N = int(input())
pattern = [['*' for _ in range(N)] for _ in range(N)]

star(N)

for i in range(N):
    result = ''
    for j in range(N):
        if pattern[i][j] == '*':
            result += pattern[i][j]
        else:
            result += ' '
    print(result)


