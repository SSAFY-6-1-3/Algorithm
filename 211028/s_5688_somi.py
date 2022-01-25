import sys
sys.stdin = open('s_5688.txt')

T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc} ', end='')
    N = int(input())
    X = round(pow(N, 1/3), 2)  # 소수점 2자리까지
    y = X % 1  # 소수점 이하의 숫자 확인
    if y:
        print(-1)
    else:
        print(int(X))
