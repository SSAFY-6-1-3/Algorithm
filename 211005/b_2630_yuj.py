import sys
sys.stdin=open('input.txt')

def divide(x, y, N):
    global white, blue

    sum_result = 0
    for i in range(x, x+N):                 # 해당 칸의 합 구하기
        for j in range(y, y+N):
            sum_result += paper[i][j]


    if sum_result == 0:                     # 합이 0이라면 모두 하얀색
        white += 1
        return

    elif sum_result == (N**2):              # 합이 N**2라면 모두 1이므로 모두 파랑색
        blue += 1
        return

    else:                                   # 4분할씩 나눠주면서 재귀
        divide(x, y, N//2)
        divide(x+N//2, y, N//2)
        divide(x, y+N//2, N//2)
        divide(x+N//2, y+N//2, N//2)




N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]

white, blue = 0, 0
divide(0, 0, N)
print(white)
print(blue)